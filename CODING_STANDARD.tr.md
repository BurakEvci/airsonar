# Kodlama Standardı

🇬🇧 [English version](CODING_STANDARD.md)

Bu belge, airsonar projesindeki her kod satırının uyduğu kuralları tanımlar ve projenin bu kurallardan
bilinçli olarak ayrıldığı her yeri kayıt altına alır. Kodda uygulanan her kural, gerekçesiyle birlikte
[uyum kaydına](docs/coding-rules/compliance-log.tr.md) işlenir.

## 1. Firmware (STM32, C++17)

### 1.1 Temel standart

**[AUTOSAR C++14 Guidelines](https://www.autosar.org/)** — *required* (zorunlu) olarak işaretlenen kurallara uyulması şarttır.

> **Doğrulanan sürüm:** Uyum kaydındaki kural kimlikleri ve ifadeleri, belgenin **Release 17-10** sürümüne göre kontrol edilmiştir. Belge "AUTOSAR CONFIDENTIAL" ibaresi taşıdığından depoya eklenmez; yalnızca bağlantı verilir.

AUTOSAR C++14, MISRA C++:2023'ün ana kaynağıdır. MISRA C++:2023 ücretli bir belge olduğundan doğrudan
kullanılmamaktadır. Bu nedenle proje kodu *MISRA uyumlu* olarak değil, *AUTOSAR C++14 kurallarına uygun*
olarak tanımlanır. Resmî bir uyumluluk beyanı, nitelikli bir araçla kural kural yapılacak tam bir kontrol gerektirir.

### 1.2 Kodun sahipliği

| Klasör | Sahibi | Kurallar |
|---|---|---|
| `App/` | Bu proje | AUTOSAR C++14'ün tamamı ve sıkı derleyici ayarları |
| `Core/`, `Drivers/` | STM32CubeMX / üretici tarafından üretilir | Kontrol edilmez (sapma D-001) |
| `Core/Src/main.c` içindeki `USER CODE` blokları | Bu proje | En aza indirilmiştir: bir `#include` ve bir `app_main()` çağrısı |

STM32CubeMX, `Core/` ve `Drivers/` klasörlerini yeniden üretir ve yalnızca `USER CODE BEGIN` ile
`USER CODE END` arasındaki kodu korur. Projenin bütün mantığı `App/` klasöründedir.

### 1.3 Dil alt kümesi

- Exception kullanılmaz (`-fno-exceptions`)
- RTTI kullanılmaz (`-fno-rtti`)
- Başlatma aşamasından sonra dinamik bellek kullanılmaz (`new`, `delete`, `malloc`, `std::vector`, `std::string`)
- `std::array`, `constexpr`, `enum class` ve sabit genişlikli tamsayı tipleri (`std::uint16_t`) tercih edilir
- Başlık dosyalarında `#pragma once` yerine include guard kullanılır (M16-2-3, A16-7-1)
- Önişlemci yalnızca dosya ekleme ve include guard için kullanılır (A16-0-1); `#ifdef __cplusplus` gibi koşullu bildirimler kullanılmaz
- Anlamı belirsiz sabit sayılar kullanılmaz: sayısal değerlere isimli bir `constexpr` sabit verilir
- Interrupt'lar ve task'lar arasında paylaşılan veriler belgelenir ve korunur

### 1.4 Derleyici ayarları

Yalnızca `App/` klasörüne uygulanır (STM32CubeIDE'de klasör düzeyinde ayar):

```
-std=c++17 -fno-exceptions -fno-rtti -fno-threadsafe-statics
-Wall -Wextra -Wpedantic -Wconversion -Wsign-conversion -Wshadow -Werror
```

`Core/` ve `Drivers/` içindeki üretilmiş kod CubeIDE'nin varsayılan ayarlarıyla derlenir, çünkü üreticinin
C kodu bu uyarılar açıkken derlenmez (D-001).

### 1.5 Doğrulama

- Yukarıdaki derleyici uyarıları, hata olarak değerlendirilir
- [`.clang-tidy`](.clang-tidy) yapılandırmasıyla `clang-tidy`
- Araçların denetleyemediği kurallar için her değişikliğin AUTOSAR C++14'e göre elle incelenmesi
- Uygulanan ya da sapılan her kural [uyum kaydına](docs/coding-rules/compliance-log.tr.md) işlenir

## 2. Bilgisayar uygulaması (Qt) ve DSP kütüphanesi

**Temel standart:** [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/).
Ortak `dsp/` kütüphanesi mikrodenetleyicide de çalıştığı için ayrıca firmware dil alt kümesine (1.3) uyar.

## 3. Sapmalar

Temel standarttan her sapma, gerekçesiyle birlikte burada kayıt altına alınır.

| ID | Kural | Kapsam | Gerekçe |
|---|---|---|---|
| D-001 | AUTOSAR C++14 (tümü) | `Core/`, `Drivers/` (STM32 HAL, CMSIS, CubeMX'in ürettiği kod) | Araçlarla yeniden üretilen ve bu projede değiştirilmeyen üretici C kodu |
| D-002 | C++14 temeli | Firmware'in tamamı | C++17 kullanılmaktadır; yalnızca C++17'de bulunan özellikler, kullanıldıkları yerde uyum kaydında belirtilir |
| D-003 | A5-2-2, M5-2-8 | `App/` içinde CubeMX/HAL makrolarının (`*_Pin`, `*_GPIO_Port`, `GPIOx`) kullanımı | Üretici makroları C tarzı cast ve tamsayıdan pointer'a dönüşüm içerir. HAL üzerinden bellek eşlemeli çevre birimi register'larına erişmenin taşınabilir tek yoludur. |
| D-004 | A18-1-1 (tavsiye) | `char const (&)[N]` biçimindeki string literal parametreleri | String literal bir C tarzı dizidir; uzunluğunu derleme anında almanın tek yolu onu referans olarak almaktır. Yalnızca literal'leri `std::array`'e çevirmek için kullanılır. |

## 4. Kural kimlikleri

Proje genelinde AUTOSAR C++14 kural kimlikleri kullanılır:

- `Ax-y-z`: AUTOSAR'ın getirdiği kurallar
- `Mx-y-z`: MISRA C++:2008'den devralınan kurallar

## 5. Commit mesajları

[Conventional Commits](https://www.conventionalcommits.org/): `tür(kapsam): özet`

Türler: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `chore` ·
Kapsamlar: `firmware`, `gui`, `fpga`, `linux`, `python`, `docs`, `hw`

Örnek: `feat(firmware): add timer-triggered ADC with DMA double buffer`

Commit mesajları, depo genelinde tutarlılık için İngilizce yazılır.
