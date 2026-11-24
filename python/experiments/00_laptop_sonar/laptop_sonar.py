"""
Experiment 00 - Laptop sonar
============================

Send an LFM chirp from the laptop speaker, record it with the laptop microphone,
apply a matched filter and measure the distance to a wall.

Usage:
    python laptop_sonar.py --simulate          # step 1: synthetic echoes, no audio hardware
    python laptop_sonar.py                     # step 2: real speaker + microphone
    python laptop_sonar.py --pings 8           # average several pings to raise SNR

The four functions marked TODO are yours to implement.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------
FS = 48_000          # sample rate [Hz]
F0 = 2_000           # chirp start frequency [Hz]
F1 = 10_000          # chirp end frequency [Hz]
T_CHIRP = 0.010      # chirp duration [s]
T_LISTEN = 0.200     # recording window per ping [s]
C_AIR = 343.0        # speed of sound in air at ~20 degC [m/s]

OUT_DIR = Path(__file__).parent / "results"


# ---------------------------------------------------------------------------
# TODO 1 - LFM chirp
# ---------------------------------------------------------------------------
def make_chirp(f0: float, f1: float, duration: float, fs: int) -> np.ndarray:
    """Return a linear frequency-modulated chirp from f0 to f1.

    Hints:
      - Time vector: t = np.arange(int(duration * fs)) / fs
      - Instantaneous frequency f(t) = f0 + k*t, with k = (f1 - f0) / duration
      - Phase is the integral of frequency: phi(t) = 2*pi*(f0*t + 0.5*k*t**2)
      - Multiply by a Tukey window (signal.windows.tukey(N, 0.1)) so the speaker
        does not "click" at the start and end.
    """
    n_samples = int(duration * fs)
    t = np.arange(n_samples) / fs
    k = (f1-f0) / duration
    phase = 2 * np.pi * (f0 * t + 0.5 * k * t**2)
    chirp = np.sin(phase)
    window = signal.windows.tukey(n_samples, 0.1)
    return chirp * window
    


# ---------------------------------------------------------------------------
# TODO 2 - Matched filter
# ---------------------------------------------------------------------------
def matched_filter(rx: np.ndarray, tx: np.ndarray) -> np.ndarray:
    return signal.correlate(rx, tx, mode="valid")

    

# ---------------------------------------------------------------------------
# TODO 3 - Envelope
# ---------------------------------------------------------------------------
def envelope(x: np.ndarray) -> np.ndarray:
    analytic = signal.hilbert(x)
    return np.abs(analytic)

# ---------------------------------------------------------------------------
# TODO 4 - Range estimation
# ---------------------------------------------------------------------------
def find_ranges(env: np.ndarray, fs: int, guard_s: float = 0.0015,
                rel_threshold: float = 0.1) -> tuple[int, list[float]]:
    """Find the direct-path peak and the echo ranges.

    Returns (direct_index, [range_m, ...]).

    Hints:
      - The laptop adds an unknown audio latency, so we cannot use the moment
        we pressed "play" as time zero. The strongest peak is the sound that
        travels directly from speaker to microphone: use it as time zero.
      - Echoes are the other peaks AFTER the direct path. Skip a guard interval
        (guard_s) right after it, otherwise the main lobe is detected as an echo.
      - signal.find_peaks(env, height=..., distance=...) finds the peaks.
        Use a height relative to the direct peak (rel_threshold * env[direct]).
      - Sound travels to the wall AND back: range = c * delay / 2
    """
    # 1) En güçlü tepe: hoparlörden mikrofona doğrudan gelen ses = zaman sıfırı
    direct = int(np.argmax(env))
    
    # 2) Eşiği geçen tüm tepeleri bul
    peaks, _ = signal.find_peaks(
        env,
        height=rel_threshold * env[direct],
        distance=int(0.0005 * fs),
    )
    
    # 3) Doğrudan sesten SONRA ve koruma aralığının dışında kalanlar = yankılar
    guard = int(guard_s * fs)
    echoes = [p for p in peaks if p > direct + guard]
    
    # 4) Gecikmeyi mesafeye çevir: ses gidip geldiği için 2'ye böl
    ranges = [(p - direct) / fs * C_AIR / 2 for p in echoes]
    return direct, ranges
    

# ---------------------------------------------------------------------------
# Provided: simulation and recording
# ---------------------------------------------------------------------------
def simulate_recording(tx: np.ndarray, fs: int, distances_m: list[float],
                       latency_s: float = 0.0373, noise_rms: float = 0.05,
                       seed: int = 0) -> np.ndarray:
    """Synthetic recording: direct path + one attenuated echo per distance + noise."""
    rng = np.random.default_rng(seed)
    rx = np.zeros(int(T_LISTEN * fs))
    paths = [(0.0, 1.0)] + [(2.0 * d / C_AIR, 0.3 / (1.0 + d)) for d in distances_m]
    for delay_s, gain in paths:
        start = int(round((latency_s + delay_s) * fs))
        rx[start:start + len(tx)] += gain * tx
    return rx + noise_rms * rng.standard_normal(len(rx))


def record_pings(tx: np.ndarray, fs: int, n_pings: int) -> np.ndarray:
    """Play the chirp n_pings times and return the coherent average of the recordings."""
    import sounddevice as sd  # imported here so --simulate works without audio drivers

    frame = np.zeros(int(T_LISTEN * fs))
    frame[:len(tx)] = 0.8 * tx
    recordings = []
    for _ in range(n_pings):
        rec = sd.playrec(frame, samplerate=fs, channels=1, blocking=True)
        recordings.append(rec[:, 0])
    # The audio latency is constant within one run, so pings line up and can be averaged.
    return np.mean(recordings, axis=0)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--simulate", action="store_true", help="use synthetic echoes")
    parser.add_argument("--distances", type=float, nargs="+", default=[0.5, 1.2],
                        help="simulated target distances [m]")
    parser.add_argument("--pings", type=int, default=4, help="number of pings to average")
    parser.add_argument("--tag", default="", help="suffix for output file names")
    args = parser.parse_args()

    tx = make_chirp(F0, F1, T_CHIRP, FS)
    if args.simulate:
        rx = simulate_recording(tx, FS, args.distances)
        mode = "simulated"
    else:
        rx = record_pings(tx, FS, args.pings)
        mode = "recorded"

    mf = matched_filter(rx, tx)
    env = envelope(mf)
    direct, ranges = find_ranges(env, FS)

    print(f"Range resolution  : {C_AIR / (2 * (F1 - F0)) * 100:.1f} cm")
    print(f"Minimum range     : {C_AIR * 0.0015 / 2 * 100:.1f} cm (guard interval)")
    print(f"Direct path index : {direct}")
    for i, r in enumerate(ranges, 1):
        print(f"Echo {i:<13}: {r:.3f} m")

    # --- plots -------------------------------------------------------------
    OUT_DIR.mkdir(exist_ok=True)
    fig, ax = plt.subplots(3, 1, figsize=(10, 9))

    t_ms = np.arange(len(rx)) / FS * 1e3
    ax[0].plot(t_ms, rx, lw=0.6)
    ax[0].set(title=f"Received signal ({mode})", xlabel="time [ms]", ylabel="amplitude")

    f, t, sxx = signal.spectrogram(rx, FS, nperseg=256, noverlap=224)
    ax[1].pcolormesh(t * 1e3, f / 1e3, 10 * np.log10(sxx + 1e-12), shading="auto")
    ax[1].set(title="Spectrogram", xlabel="time [ms]", ylabel="frequency [kHz]", ylim=(0, 14))

    dist_m = (np.arange(len(env)) - direct) / FS * C_AIR / 2
    env_db = 20 * np.log10(env / env[direct] + 1e-9)
    ax[2].plot(dist_m, env_db, lw=0.8)
    for r in ranges:
        ax[2].axvline(r, color="tab:red", ls="--", lw=0.8)
    ax[2].set(title="Matched filter output (A-scan)", xlabel="range [m]",
              ylabel="relative level [dB]", xlim=(-0.2, 3.0), ylim=(-40, 3))

    fig.tight_layout()
    out = OUT_DIR / f"ascan_{mode}{'_' + args.tag if args.tag else ''}.png"
    fig.savefig(out, dpi=120)
    print(f"Plot saved        : {out}")
    plt.show()


if __name__ == "__main__":
    main()
