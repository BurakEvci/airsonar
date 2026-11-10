# Hardware

## Bill of materials

| Part | Qty | Notes |
|---|---|---|
| STM32 Nucleo-F446RE | 1 | Cortex-M4F @ 180 MHz, 12-bit ADC and DAC |
| ZedBoard (Zynq XC7Z020) | 1 | Phase 4 and FPGA track |
| MAX9814 microphone module | 2 | Output biased within 0–3.3 V |
| PAM8403 amplifier + small speaker | 1 | Driven by the F446RE DAC |
| USB logic analyzer (8 ch) | 1 | sigrok / PulseView |

## Pin plan (Nucleo-F446RE)

| Function | Pin | Note |
|---|---|---|
| User LED (LD2) | PA5 | Conflicts with SPI1 SCK → SPI2 is used |
| User button (B1) | PC13 | |
| UART to PC (ST-LINK VCP) | PA2 / PA3 | USART2 |
| SPI2 SCK / MISO / MOSI | PB13 / PB14 / PB15 | |
| I2C1 SCL / SDA | PB8 / PB9 | Arduino D15 / D14 |
| DAC out | PA4 | DAC channel 1 |

⚠️ ADC inputs accept **0–3.3 V only**.
