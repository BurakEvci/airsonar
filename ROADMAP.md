# Roadmap

Pace: ~8–10 hours/week. Each week ends with a report in [`docs/reports/`](docs/reports).
A parallel FPGA track on the ZedBoard (one evening per week) starts in week 5.

## Phase 0 — Warm-up

| Week | Implementation | Done |
|---|---|---|
| 0 | Laptop sonar in Python: chirp, matched filter, envelope, range | 🟡 wall measurement pending |

## Phase 1 — Embedded foundations (Nucleo-F446RE + Qt)

| Week | Implementation | Theory | Done |
|---|---|---|---|
| 1 | Toolchain, C++ project, LED blink, UART output | MCU architecture, clock tree, memory map | ✅ |
| 2 | Register-level GPIO, button interrupt, timer interrupt | NVIC, `volatile`, ISR rules | ☐ |
| 3 | Timer-triggered ADC + DMA double buffer, jitter measurement | Sampling theorem, aliasing, DMA | ☐ |
| 4 | Qt app: serial port, packet format, live plot, FFT | DFT/FFT, windowing, STFT, spectrogram | ☐ |
| | **Milestone `v0.1-live-spectrum`** · video | | ☐ |
| 5 | SPI: loopback, external ADC, register-level driver | SPI modes (CPOL/CPHA) | ☐ |
| 6 | I2C sensor: bus scan, register access, error handling | I2C protocol, ACK/NACK, pull-ups | ☐ |
| 7 | FreeRTOS: tasks, queues, priorities | Scheduling, priority inversion, deadlines | ☐ |
| 8 | FIR/IIR on MCU (CMSIS-DSP), coding-standard pass, cleanup | FIR/IIR design, decimation | ☐ |
| | **Milestone `v0.2-data-node`** · video · LinkedIn post | | ☐ |

## Phase 2 — Active sonar (~5 weeks)

DAC chirp output, LFM pulse compression, matched filter, cross/auto-correlation, thresholding, CFAR,
SNR estimation, two-microphone TDOA, delay-and-sum beamforming, Doppler estimation; A-scan and waterfall views in Qt.

**Milestone `v0.3-sonar-ranging`** · video · LinkedIn post

## Phase 3 — Acoustic modem (~8 weeks)

Carrier/baseband/passband, up/down conversion, I/Q, Hilbert transform and analytic signal, envelope detection,
FSK with Goertzel, BPSK/DPSK/QPSK, RRC pulse shaping, preamble detection, symbol timing recovery,
Costas loop/PLL, CFO estimation, ISI and LMS equalization, constellation and eye diagrams, BER,
CRC, Hamming, convolutional codes + Viterbi, interleaving.

**Milestone `v0.4-acoustic-modem`** · video · LinkedIn post

## Parallel track — FPGA basics (ZedBoard, from week 5)

Verilog basics (LED, counter, UART), simulation and testbenches, timing constraints, ILA,
I2S receiver for the on-board ADAU1761 codec, SPI slave.

## Phase 4 — Zynq system integration

Nucleo as sensor node over SPI → FPGA (FIR / FFT / matched filter) → AXI DMA → PREEMPT_RT Linux with a
custom kernel driver → Ethernet → Qt. Advanced topics: polyphase filter banks, OFDM + cyclic prefix,
MVDR, MUSIC/ESPRIT, RLS, Reed-Solomon, LDPC.

**Milestone `v1.0-zynq-system`** · video · LinkedIn post
