import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from laptop_sonar import make_chirp, matched_filter, FS
from laptop_sonar import envelope

# buraya matched_filter_slow fonksiyonunu yaz
def matched_filter_slow(rx, tx):
    n_out = len(rx) - len(tx) + 1        # chirp'in sığabileceği başlangıç noktası sayısı
    out = np.zeros(n_out)
    for i in range(n_out):
        segment = rx[i : i + len(tx)]    # kayıttan chirp uzunluğunda bir parça
        out[i] = np.sum(segment * tx)    # karşılıklı çarp ve topla
    return out


tx = make_chirp(2000, 10000, 0.010, FS)

# Sahte kayıt: 2000 örnek, chirp 700. örnekte başlıyor, üstüne GÜÇLÜ gürültü
rng = np.random.default_rng(0)
rx = np.zeros(2000)
rx[700 : 700 + len(tx)] += tx
rx += 2.0 * rng.standard_normal(2000)

fast = matched_filter(rx, tx)
slow = matched_filter_slow(rx, tx)

print("Aynı mı?:", np.allclose(fast, slow))
print("Tepe noktası:", np.argmax(fast))

for method in ["direct", "fft"]:
    t0 = time.perf_counter()
    for _ in range(200):
        signal.correlate(rx, tx, mode="valid", method=method)
    print(method, f"{(time.perf_counter() - t0) / 200 * 1e6:.0f} µs")

fig, ax = plt.subplots(2, 1)
ax[0].plot(rx);   ax[0].set_title("Kayıt (chirp gürültünün içinde)")
ax[1].plot(fast); ax[1].set_title("Matched filter çıkışı")
plt.tight_layout(); plt.show()

env = envelope(fast)
print("Zarfın tepe noktası:", np.argmax(env))

plt.figure()
plt.plot(fast, label="matched_filter")
plt.plot(env, label="zarf", lw=2)
plt.xlim(650,750)
plt.legend(); plt.show()
