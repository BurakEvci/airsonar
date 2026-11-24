import matplotlib.pyplot as plt
import sounddevice as sd
from laptop_sonar import make_chirp, FS

c = make_chirp(2000, 10000, 0.010, FS)
print(len(c))            # kaç çıkmalı?
plt.plot(c)
plt.show()

# Chirp'i duy: 1 saniyelik, daha yavaş bir versiyon
slow = make_chirp(200, 2000, 1.0, FS)
sd.play(0.3 * slow, FS)
sd.wait()