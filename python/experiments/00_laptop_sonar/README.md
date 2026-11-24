# Experiment 00 — Laptop sonar

Measure the distance to a wall using only a laptop speaker and microphone:
LFM chirp → recording → matched filter → envelope → range.

## Steps

1. Implement the four `TODO` functions in [`laptop_sonar.py`](laptop_sonar.py).
2. Validate on synthetic data — no audio hardware involved:
   ```bash
   python laptop_sonar.py --simulate
   python laptop_sonar.py --simulate --distances 0.3 0.8 2.0
   ```
   Expected: echoes reported at the simulated distances (±1 cm).
3. Real measurement: place the laptop facing a wall at 0.5 m, 1.0 m and 1.5 m (tape measure).
   ```bash
   python laptop_sonar.py --pings 8 --tag wall_050cm
   ```
4. Record measured vs. true distance in `results/measurements.csv`:
   ```
   true_m,measured_m,pings,notes
   0.50,,8,
   ```

## Before the real measurement

- Disable microphone **noise suppression / echo cancellation / audio enhancements**
  in the OS sound settings — they are designed to remove exactly the signal we want.
- Moderate volume. Close music and video calls.
- The laptop speaker and microphone are not at the same point, so expect a few cm of
  geometric offset.

## Key numbers

| Quantity | Formula | Value |
|---|---|---|
| Range resolution | c / (2B) | 343 / (2 · 8000) ≈ 2.1 cm |
| Minimum range | c · guard / 2 | ≈ 26 cm |
| Time-bandwidth product | T · B | 0.010 · 8000 = 80 |
