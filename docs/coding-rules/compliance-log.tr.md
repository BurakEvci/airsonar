# Kodlama Kuralları Uyum Kaydı

🇬🇧 [English version](compliance-log.md) · Standart: [CODING_STANDARD.tr.md](../../CODING_STANDARD.tr.md)

`App/` klasöründe uygulanan her AUTOSAR C++14 kuralı, uyumu etkileyen her tasarım kararı ve her sapma
kullanımı burada kayıt altına alınır. Commit'lenen kayıtlar silinmez; kod değişirse, eski kayda atıf yapan
yeni bir kayıt eklenir. Kural kimlikleri ve ifadeleri AUTOSAR C++14 Guidelines **Release 17-10** sürümüne
göre doğrulanmıştır.

**Kayıt türleri:** ✅ kural uygulandı · ⚠️ sapma kullanıldı (bkz. CODING_STANDARD.tr.md §3) · 💡 tasarım kararı (kural kimliği yok)

## Özet

| ID | Hafta | Dosya | Tür | Kural | Karar |
|---|---|---|---|---|---|
| CR-001 | 1 | `App/Inc/app.hpp`, `app.h` | ✅ | M16-2-3, A16-7-1 | `#pragma once` yerine include guard |
| CR-002 | 1 | `App/Inc/app.hpp`, `app.h` | ✅ | A16-0-1 | `#ifdef __cplusplus` yerine ayrı C ve C++ başlık dosyaları |
| CR-003 | 1 | `App/Inc/app.hpp` | ✅ | A3-3-1 | `app_main()` bir başlık dosyasında bildirildi |
| CR-004 | 1 | `App/Src/app.cpp` | ✅ | A5-1-1, A7-1-2 | `500` sabiti yerine isimli `constexpr` sabit |
| CR-005 | 1 | `App/Src/app.cpp` | ✅ | M3-4-1 | Sabit, onu kullanan fonksiyonun içinde tanımlandı |
| CR-006 | 1 | `App/Src/app.cpp` | ✅ | M5-0-4 | İşaretsiz sabit `500U` |
| CR-007 | 1 | `App/Src/app.cpp` | ✅ | A3-9-1 | Sabit genişlikli tamsayı tipleri |
| CR-008 | 1 | `App/Src/app.cpp` | ✅ | A8-5-2 | Süslü parantezle ilk değer atama |
| CR-009 | 1 | `App/Inc/app.hpp`, `App/Src/app.cpp` | ✅ | A15-4-4 | Exception fırlatmayan fonksiyonlarda `noexcept` |
| CR-010 | 1 | `App/Src/app.cpp` | ✅ | A3-3-1, M7-3-3 | `Led` sınıfı `.cpp` dosyasında isimsiz namespace içinde |
| CR-011 | 1 | `App/Src/app.cpp` | ✅ | A7-1-1 | `Led`'in veri üyeleri `const` |
| CR-012 | 1 | `App/Src/app.cpp` | ✅ | A12-4-2 (tavsiye) | `Led` sınıfı `final` |
| CR-013 | 1 | `App/Src/app.cpp` | 💡 | — | `Led::toggle()` `const` değil |
| CR-014 | 1 | `App/Inc/app.h`, `app.hpp` | 💡 | — | `app_main()`'in iki bildirimi uyumlu tutulmalı |
| CR-015 | 1 | `App/Src/app.cpp` | ⚠️ | D-003 | HAL makroları `LD2_GPIO_Port`, `LD2_Pin` kullanıldı |
| CR-016 | 1 | `App/Src/app.cpp` | ✅ | M27-0-1 | `<cstdio>` / `printf` yok; çıktı bir `Uart` sınıfı üzerinden |
| CR-017 | 1 | `App/Src/app.cpp` | ✅ | A5-2-3, A5-2-4 | Metin `to_bytes()` ile bayta çevrildi, pointer cast'i yok |
| CR-018 | 1 | `App/Src/app.cpp` | ⚠️ | D-004 | `to_bytes()` string literal'i `char const (&)[N]` olarak alıyor |
| CR-019 | 1 | `App/Src/app.cpp` | ✅ | A4-7-1 | `static_assert`, uzunluğun `std::uint16_t`'ye sığdığını kanıtlıyor |
| CR-020 | 1 | `App/Src/app.cpp` | ✅ | A0-1-2 | `Uart::write()` sonucu `static_cast<void>` ile bilinçli olarak yok sayıldı |
| CR-021 | 1 | `App/Src/app.cpp` | ✅ | A7-1-5 | `auto` yalnızca `to_bytes()` sonucu için |
| CR-022 | 1 | `App/Src/app.cpp` | ✅ | A7-1-3 | cv-belirteçleri typedef isimlerinin sağında |
| CR-023 | 1 | `App/Src/app.cpp` | 💡 | — | `Uart` yapıcısı `explicit` |
| CR-024 | 1 | `.clang-tidy` | 💡 | — | clang-tidy'nin C++ Core Guidelines C.12 kontrolü yerine AUTOSAR A7-1-1 esas alındı |
| CR-025 | 1 | `App/Src/app.cpp` | 💡 | — | Bloklayan UART gönderimi şimdilik kabul edildi |
| CR-026 | 1 | `App/Lib/Inc/text_format.hpp` | ✅ | M7-3-1 | `to_decimal()` global namespace'te değil, `airsonar::lib` içinde |
| CR-027 | 1 | `App/Lib/Src/text_format.cpp` | ✅ | A6-5-3 (tavsiye) | `do … while` yerine `count == 0U` koşullu `while` |
| CR-028 | 1 | `App/Src/app.cpp`, `App/Lib/Src/text_format.cpp` | ✅ | A4-7-1 | Sayacın açık başa dönüşü; aritmetik aralıkları kanıtlandı |
| CR-029 | 1 | `App/Src/app.cpp`, `App/Lib/Src/text_format.cpp` | ✅ | A5-2-5 | Dizi indisleri ve uzunluklar dizi boyutuna göre denetlendi |
| CR-030 | 1 | `App/Lib/` | 💡 | — | Kütüphane katmanı HAL / CubeMX başlık dosyalarını hiç eklemez |
| CR-031 | 1 | `App/Lib/` | 💡 | — | C++17 `namespace a::b` yerine klasik iç içe namespace |
| CR-032 | 1 | `App/Src/app.cpp` | 💡 | — | `Uart::write(data)`, `write(data, length)` fonksiyonunu çağırır |

## Hafta 1 — İlk C++ firmware (`app_main`, yanıp sönen LED)

Bu hafta incelenen son kod:

```cpp
// App/Inc/app.h — C arayüzü, Core/Src/main.c tarafından eklenir
#ifndef AIRSONAR_APP_H
#define AIRSONAR_APP_H
/* C++ declaration: app.hpp. Keep both in sync (CR-014). */
void app_main(void);
#endif
```

```cpp
// App/Inc/app.hpp — C++ bildirimi, App/Src/app.cpp tarafından eklenir
#ifndef AIRSONAR_APP_HPP
#define AIRSONAR_APP_HPP
// C declaration: app.h. Keep both in sync (CR-014).
extern "C" void app_main() noexcept;
#endif
```

```cpp
// App/Src/app.cpp
#include "app.hpp"
#include "main.h"
#include <cstdint>

namespace {

class Led final {
public:
    Led(GPIO_TypeDef* const port, std::uint16_t const pin) noexcept : port_{port}, pin_{pin} {}
    void toggle() noexcept { HAL_GPIO_TogglePin(port_, pin_); }

private:
    GPIO_TypeDef* const port_;
    std::uint16_t const pin_;
};

}  // namespace

extern "C" void app_main() noexcept
{
    constexpr std::uint32_t kLedToggleIntervalMs{500U};
    Led led{LD2_GPIO_Port, LD2_Pin};
    while (true) {
        led.toggle();
        HAL_Delay(kLedToggleIntervalMs);
    }
}
```

### CR-001 · M16-2-3, A16-7-1 · `#pragma once` yerine include guard

*Kurallar:* Include guard kullanılmalıdır (M16-2-3). `#pragma` direktifi kullanılmamalıdır (A16-7-1).
*Önce:* `#pragma once`
*Sonra:* `#ifndef AIRSONAR_APP_HPP` / `#define AIRSONAR_APP_HPP` / `#endif`
*Gerekçe:* `#pragma`'nın davranışı derleyiciye bağlıdır. Include guard standart C++'tır ve her derleyicide
çalışır. Çakışmayı önlemek için guard adları proje adıyla başlar.

### CR-002 · A16-0-1 · Ayrı C ve C++ başlık dosyaları

*Kural:* Önişlemci yalnızca koşulsuz ve koşullu dosya ekleme ile include guard için, belirli bir direktif
listesiyle kullanılmalıdır. Kuralın kendi örneği, `#ifdef` içindeki bir bildirimi uyumsuz olarak gösterir.
*Önce:* bildirimin `#ifdef __cplusplus extern "C" { ... } #endif` içine alındığı tek bir başlık dosyası.
*Sonra:* iki başlık dosyası: `app.h` (düz C, `main.c` için) ve `app.hpp` (C++, `extern "C" ... noexcept`).
*Gerekçe:* Yaygın tek başlık dosyası yöntemi, koşullu derlemeyi dosya eklemek için değil bir bildirim için
kullanır. İki ayrı başlık dosyası, önişlemci kullanımını yalnızca include guard ile sınırlı tutar. Ayrıca C++
bildiriminin C'de geçersiz olan `noexcept` belirtecini taşımasını sağlar (CR-009). Bu seçimin bedeli için bkz. CR-014.

### CR-003 · A3-3-1 · `app_main()` bir başlık dosyasında bildirildi

*Kural:* Dış bağlantılı nesne ve fonksiyonlar (isimli namespace üyeleri dahil) bir başlık dosyasında bildirilmelidir.
*Sonra:* `app_main()`, `app.hpp` içinde bildirilmiş ve `app.cpp` içinde C bağlantısıyla tanımlanmıştır.
Böylece C dosyası olan `main.c`, C++'ın isim dönüştürmesine (name mangling) takılmadan fonksiyonu çağırabilir.
*Gerekçe:* Başlık dosyasındaki tek bir bildirim, tanımın ve bütün C++ çağrılarının aynı fonksiyon imzasını kullanmasını garanti eder.

### CR-004 · A5-1-1, A7-1-2 · Sabit sayı yerine isimli sabit

*Kurallar:* Sayısal değerler, tip ilk değer ataması dışında kullanılmamalı, bunun yerine sembolik isimler
kullanılmalıdır (A5-1-1). Derleme zamanında belirlenebilen değerler için `constexpr` kullanılmalıdır (A7-1-2).
*Önce:* `HAL_Delay(500);`
*Sonra:* `constexpr std::uint32_t kLedToggleIntervalMs{500U};` ve ardından `HAL_Delay(kLedToggleIntervalMs);`
*Gerekçe:* İsim, sayının ne anlama geldiğini ve birimini (ms) belirtir.

### CR-005 · M3-4-1 · Sabit, kullanıldığı yerde tanımlandı

*Kural:* Bir nesne ya da tip olarak bildirilen tanımlayıcı, görünürlüğünü en aza indiren blokta tanımlanmalıdır.
*Önce (ilk taslak):* `kLedToggleIntervalMs` namespace kapsamında.
*Sonra:* onu kullanan tek fonksiyon olan `app_main()` içinde tanımlandı.
*Gerekçe:* Kapsam ne kadar dar olursa, tanımlayıcıya bağımlı olabilecek ya da onu yanlış kullanabilecek yer o kadar az olur.

### CR-006 · M5-0-4 · İşaretsiz sabit `500U`

*Kural:* Örtük tamsayı dönüşümü, tipin işaretliliğini değiştirmemelidir.
*Önce:* `500` (`int`, işaretli) ile bir `std::uint32_t` değişkene ilk değer atanıyor.
*Sonra:* `500U` (`unsigned int`).
*Gerekçe:* İşaretliden işaretsize örtük bir dönüşüm yapılmaz.

### CR-007 · A3-9-1 · Sabit genişlikli tamsayı tipleri

*Kural:* Temel sayısal tipler yerine, boyutu ve işaretliliği belirten `<cstdint>` tipleri kullanılmalıdır.
*Sonra:* Gecikme için `std::uint32_t`, pin maskesi için `std::uint16_t`.
*Gerekçe:* `int`'in boyutu platforma göre değişir; mikrodenetleyicide register genişlikleri önemlidir.
`std::uint16_t`, HAL'in pin tipiyle aynıdır.

### CR-008 · A8-5-2 · Süslü parantezle ilk değer atama

*Kural:* Değişkenlere ilk değer, eşittir işareti olmadan süslü parantezle `{}` atanmalıdır.
*Sonra:* `kLedToggleIntervalMs{500U}`, `port_{port}`, `pin_{pin}`, `Led led{LD2_GPIO_Port, LD2_Pin};`
*Gerekçe:* Süslü parantezle atama, daraltan dönüşümleri derleme anında reddeder ve tüm tipler için tek bir yazım sunar.

### CR-009 · A15-4-4 · Exception fırlatmayan fonksiyonlarda `noexcept`

*Kural:* Exception fırlatmayan bir fonksiyonun bildiriminde `noexcept` belirtilmelidir.
*Sonra:* `Led` yapıcısı, `Led::toggle()` ve `app_main()` `noexcept` olarak işaretlenmiştir.
*Gerekçe:* Firmware `-fno-exceptions` ile derlendiği için hiçbir kod exception fırlatamaz. `noexcept` bunu
belgeler ve optimizasyona izin verir. `app_main()` bu belirteci yalnızca C++ başlık dosyasında taşıyabilir (CR-002).

### CR-010 · A3-3-1, M7-3-3 · Yardımcı sınıf isimsiz namespace içinde

*Kurallar:* A3-3-1 (yukarıda). Başlık dosyalarında isimsiz namespace bulunmamalıdır (M7-3-3).
*Sonra:* `Led`, `app.cpp` içinde `namespace { ... }` bloğunda tanımlanmıştır.
*Gerekçe:* `Led` yalnızca `app.cpp` içinde kullanılır. İsimsiz namespace ona iç bağlantı verir; böylece
başlık dosyasında bildirilmesi gerekmez ve başka dosyalardaki isimlerle çakışamaz. İsimsiz namespace yalnızca
başlık dosyalarında yasaktır.

### CR-011 · A7-1-1 · `const` veri üyeleri

*Kural:* Değişmeyen veriler `constexpr` ya da `const` belirteciyle bildirilmelidir.
*Önce (ilk taslak):* `GPIO_TypeDef* port_;` ve `std::uint16_t pin_;`
*Sonra:* `GPIO_TypeDef* const port_;` ve `std::uint16_t const pin_;`
*Gerekçe:* Bir `Led` nesnesi ömrü boyunca tek bir pine bağlıdır; üyeleri oluşturulduktan sonra hiç değişmez.
`const` bunu derleyiciye denetletir. Yan etkisi: `Led` nesnelerine kopyalayarak atama yapılamaz; bu da istenen bir durumdur.

### CR-012 · A12-4-2 (tavsiye) · `Led` sınıfı `final`

*Kural:* Bir sınıfın public yıkıcısı sanal (virtual) değilse, sınıf `final` olarak bildirilmelidir.
*Sonra:* `class Led final`
*Gerekçe:* `Led`'in örtük ve sanal olmayan bir yıkıcısı vardır ve temel sınıf olarak tasarlanmamıştır.
Türetilmiş bir nesneyi temel sınıf pointer'ı üzerinden silmek tanımsız davranıştır; `final` kalıtımı tamamen engeller.

### CR-013 · 💡 · `Led::toggle()` `const` değil

*Önce (ilk taslak):* `void toggle() const noexcept`
*Sonra:* `void toggle() noexcept`
*Gerekçe:* İlk sürümü yasaklayan bir kural yoktur; hiçbir veri üyesi değişmediği için derleyici de kabul eder.
Ancak fonksiyon, nesnenin temsil ettiği donanımın durumunu değiştirir. `const` işareti, okuyana fonksiyonu
çağırmanın görünür bir etkisi olmadığını söylerdi; bu doğru değildir (*mantıksal sabitlik*, logical constness).

### CR-014 · 💡 · `app_main()`'in iki bildirimi

*Karar:* CR-002 aynı fonksiyon için iki bildirim getirir: `app.h` içinde `void app_main(void);` (C olarak
derlenir) ve `app.hpp` içinde `extern "C" void app_main() noexcept;` (C++ olarak derlenir).
*Risk:* C ve C++ derleyicileri birbirlerinin bildirimini hiç görmez; bağlayıcı (linker) da C fonksiyonlarını
yalnızca isimle eşleştirir. Bir uyumsuzluk derleme sırasında fark edilmez.
*Önlem:* Fonksiyon parametre almaz ve değer döndürmez, yani uyumsuzluk olabilecek bir şey yoktur. İki başlık
dosyası da birbirini gösteren bir açıklama satırı içerir. İmzada ileride yapılacak her değişiklik, iki dosyada
aynı commit içinde güncellenmelidir.

### CR-015 · ⚠️ D-003 · HAL makroları `LD2_GPIO_Port`, `LD2_Pin`

*Etkilenen kurallar:* Geleneksel C tarzı cast kullanılmamalıdır (A5-2-2). Tamsayı tipindeki ya da `void`
pointer tipindeki bir nesne, pointer tipine dönüştürülmemelidir (M5-2-8).
*Kod:* `Led led{LD2_GPIO_Port, LD2_Pin};`
*Sapmanın gerekçesi:* CubeMX `#define LD2_GPIO_Port GPIOA` satırını üretir; CMSIS `GPIOA`'yı
`((GPIO_TypeDef *) GPIOA_BASE)` olarak tanımlar. Bu, tamsayı bir adresten pointer'a C tarzı bir cast'tir.
Bellek eşlemeli register'lara üreticinin başlık dosyaları üzerinden bu şekilde erişilir.
*Sınırlandırma:* Makrolar yalnızca bir `Led` nesnesi oluşturulurken kullanılır. Kodun geri kalanı, nesnede
saklanan tipli `GPIO_TypeDef*` ve `std::uint16_t` değerleriyle çalışır.

### UART çıktısı (CR-016 … CR-025)

Kod için İngilizce kayda bakınız: [compliance-log.md](compliance-log.md) (kod blokları aynıdır).

### CR-016 · M27-0-1 · `<cstdio>` kullanılmadı

*Kural:* `<cstdio>` giriş/çıkış kütüphanesi kullanılmamalıdır.
*Karar:* `printf` kullanılmaz. Metin, küçük bir `Uart` sınıfı aracılığıyla `HAL_UART_Transmit` ile gönderilir.
*Gerekçe:* `printf` argümanlarının tipini denetlemez (format dizisi hataları), değişken sayıda argüman alan bir
arayüz kullanır ve mikrodenetleyicide büyük bir biçimlendirme kütüphanesini, çoğu zaman da dinamik belleği beraberinde getirir.

### CR-017 · A5-2-3, A5-2-4 · Pointer cast'i olmadan metinden bayta

*Kurallar:* Bir cast, pointer ya da referans tipinden `const` veya `volatile` niteliğini kaldırmamalıdır
(A5-2-3). `reinterpret_cast` kullanılmamalıdır (A5-2-4).
*Sorun:* `HAL_UART_Transmit` `const uint8_t*` alır, string literal ise `const char[]` tipindedir. Yaygın
`(uint8_t*)"metin"` yazımı C tarzı bir cast'tir, `reinterpret_cast<const uint8_t*>` ise A5-2-4 ile yasaktır.
*Sonra:* `constexpr` fonksiyon `to_bytes()`, her karakteri `static_cast<std::uint8_t>` ile derleme anında bir
`std::array<std::uint8_t, N - 1>` içine kopyalar. Hiçbir pointer cast edilmez; dizinin `data()` fonksiyonu zaten doğru tipi döndürür.
*Ek fayda:* Dönüşüm derleme anında yapıldığı için çalışma zamanında hiçbir maliyeti yoktur.

### CR-018 · ⚠️ D-004 · String literal parametresi

*Etkilenen kural:* C tarzı diziler kullanılmamalıdır (A18-1-1, tavsiye).
*Kod:* `to_bytes(char const (&text)[N])`
*Gerekçe:* String literal'in kendisi bir C tarzı dizidir. Uzunluğu `N`'yi derleme anında alabilmenin tek yolu,
onu diziye referans olarak almaktır. Dizi yalnızca `to_bytes()` içinde okunur; kodun geri kalanı `std::array` kullanır.

### CR-019 · A4-7-1 · Uzunluk `std::uint16_t`'ye sığıyor

*Kural:* Bir tamsayı ifadesi veri kaybına yol açmamalıdır.
*Kod:* `static_assert(N <= kMaxFrameSize, ...)` ve ardından `static_cast<std::uint16_t>(N)`.
*Gerekçe:* `HAL_UART_Transmit` uzunluğu `uint16_t` olarak alır. `static_assert`, `N`'nin bu tipe sığdığını
derleme anında kanıtlar; böylece cast hiçbir zaman veri kaybettiremez. 65 535 bayttan uzun bir mesaj derlenmez.

### CR-020 · A0-1-2 · Dönüş değeri bilinçli olarak yok sayıldı

*Kural:* `void` olmayan bir dönüş tipine sahip ve aşırı yüklenmiş bir operatör olmayan fonksiyonun döndürdüğü
değer kullanılmalıdır. Kural, değerin `static_cast<void>` ile yok sayılmasına izin verir.
*Kod:* `static_cast<void>(uart.write(kTickMessage));`
*Gerekçe:* Bu çıktı yalnızca tanılama amaçlıdır. Başarısız bir gönderim firmware'i durdurmamalıdır; bu yüzden
sonuç bilinçli olarak yok sayılır ve cast bu kararı kodda görünür kılar.

### CR-021 · A7-1-5 · Fonksiyon sonucu için `auto`

*Kural:* `auto` yalnızca listelenen durumlarda kullanılmalıdır; bunlardan biri (1) bir fonksiyon çağrısının
dönüş tipiyle aynı tipte bir değişkendir.
*Kod:* `constexpr auto kBootMessage{to_bytes("airsonar: boot\r\n")};`
*Gerekçe:* Tip `std::array<std::uint8_t, 16>`'dır. Uzunluğu elle yazmak, metin her değiştiğinde güncelleme
gerektirirdi; `auto` tipi `to_bytes()`'tan alır.

### CR-022 · A7-1-3 · cv-belirteçleri sağda

*Kural:* cv-belirteçleri, typedef ya da using ismi olan tipin sağ tarafına yazılmalıdır.
*Kod:* `std::uint16_t const pin`, `std::array<...> const& data`, `HAL_StatusTypeDef const status`.
*Gerekçe:* `std::uint16_t` ve `HAL_StatusTypeDef` typedef isimleridir. `const`'u sağa yazmak, ifadenin sağdan
sola tutarlı okunmasını sağlar ve pointer typedef'lerindeki `const`'un klasik yanlış okunmasını önler.

### CR-023 · 💡 · `explicit` yapıcı

*Kod:* `explicit Uart(UART_HandleTypeDef& handle) noexcept`
*Gerekçe:* A12-1-4, `explicit`'i yalnızca *temel* (fundamental) tipte tek argüman alan yapıcılar için zorunlu
tutar; `UART_HandleTypeDef&` temel bir tip değildir. Yine de bir `UART_HandleTypeDef`'in fark edilmeden bir
`Uart` nesnesine dönüşmemesi için `explicit` kullanılmıştır (C++ Core Guidelines C.46).

### CR-024 · 💡 · Araç çelişkisi: AUTOSAR A7-1-1 ve C++ Core Guidelines C.12

*Bulgu:* clang-tidy'nin `cppcoreguidelines-avoid-const-or-ref-data-members` kontrolü (C.12: "veri üyelerini
const ya da referans yapmayın"), `Led::port_`, `Led::pin_` ve `Uart::handle_` için uyarı verir.
*Karar:* Firmware'in temel standardı AUTOSAR C++14'tür (CODING_STANDARD.tr.md §1.1). A7-1-1 değişmeyen veriler
için `const` ister (CR-011) ve bu nesnelerin kopyalanarak atanamaması bilinçli bir tercihtir. Bu kontrol
firmware için `.clang-tidy` dosyasında kapatılmıştır.
*Ders:* Kodlama standartları birbiriyle çelişebilir. Proje tek bir temel standart seçer ve çelişkiyi kayda geçirir.

### CR-025 · 💡 · Bloklayan gönderim

*Karar:* `HAL_UART_Transmit`, bütün baytlar gönderilene kadar işlemciyi bekletir.
*Maliyet:* 115 200 baud'da bir bayt 10 bit / 115 200 ≈ 87 µs sürer. 16 baytlık açılış mesajı ≈ 1,4 ms,
6 baytlık tick mesajı ise her 500 ms'de ≈ 0,5 ms bekletir.
*Neden şimdilik kabul edilebilir:* Henüz başka bir iş çalışmıyor. Örneklemenin gecikmemesi gereken Hafta 3'te gönderim DMA'ya taşınacak.

### Tick sayacı ve `to_decimal()` (CR-026 … CR-032)

Kod için İngilizce kayda bakınız: [compliance-log.md](compliance-log.md). Bilgisayarda sıkı derleyici ayarlarıyla
test edilmiştir: 0, 7, 10, 42, 472, 1000 ve 4 294 967 295 doğru dönüştürülmektedir.

### CR-026 · M7-3-1 · Global namespace'te fonksiyon yok

*Kural:* Global namespace yalnızca `main`, namespace bildirimleri ve `extern "C"` bildirimleri içermelidir.
*Sonra:* `to_decimal()` ve `kMaxDecimalDigits`, `namespace airsonar { namespace lib { … } }` içindedir.
*Gerekçe:* Global namespace'teki isimler, HAL'in C fonksiyonları dahil herhangi bir kütüphaneyle çakışabilir.

### CR-027 · A6-5-3 (tavsiye) · `do` deyimi yok

*Kural:* `do` deyimleri kullanılmamalıdır.
*Kod:* `while ((remaining > 0U) || (count == 0U))`
*Gerekçe:* 0'ı dönüştürmek için döngü gövdesinin en az bir kez çalışması gerekir; bu, `do … while`'ın klasik
kullanım alanıdır. Ek `count == 0U` koşulu, aynı garantiyi koşulu en üstte görünen düz bir `while` ile sağlar.

### CR-028 · A4-7-1 · Tamsayı ifadelerinde veri kaybı yok

*Kural:* Bir tamsayı ifadesi veri kaybına yol açmamalıdır. Kural, başa dönmeyi (wrap-around) açıkça kapsar.
*Durumlar:*
- `++tick_count`, 4 294 967 295'ten 0'a dönerdi. `next_count()` bu dönüşü bir aralık denetimiyle açık hale getirir.
  500 ms'de bir tick ile dönüş yaklaşık 68 yıl sonra gerçekleşir; denetim, bunun hiç olmayacağına güvenmek yerine davranışı belgeler.
- `static_cast<std::uint8_t>(kAsciiZero + digit)`: `digit`, `remaining % 10` olduğundan 0–9 arasındadır; sonuç 48–57 arasındadır ve `std::uint8_t`'ye sığar.
- `count - 1U - i`: Döngü yalnızca `i < count` iken çalıştığından sonuç en az 0'dır ve hiçbir zaman başa dönmez.

### CR-029 · A5-2-5 · Dizi sınırları dışına erişim yok

*Kural:* Bir diziye sınırları dışında erişilmemelidir.
*Durumlar:*
- `Uart::write(data, length)`, HAL'i çağırmadan önce `length <= N` koşulunu denetler, aksi halde `false` döndürür.
- `to_decimal()` içinde `count` en fazla 10 olabilir; çünkü `std::uint32_t` en fazla 10 basamaklıdır ve bu, `kMaxDecimalDigits`'e eşittir.
*Uygulamada gözlenen:* Öğrenme sürecinde `count - 1U - i` yerine `count - 1U - 1` indeksi denenmiştir. Tek basamaklı
bir sayı için bu ifade `SIZE_MAX` değerini alır ve dizinin dışındaki belleği okur; test rastgele karakterler
(`"O"`, `"U"`) yazdırmıştır. A5-2-5'in hedeflediği hata türü tam olarak budur ve yalnızca belirli girdilerde ortaya çıkar.

### CR-030 · 💡 · Donanım bağımlılığı olmayan kütüphane katmanı

*Karar:* `App/Lib/` içindeki kod yalnızca standart başlık dosyalarını ekler; `main.h`, `usart.h` ya da herhangi bir HAL başlık dosyasını asla eklemez.
*Gerekçe:* Böylece kütüphane kodu bilgisayarda derlenip birim testlerinden geçirilebilir, Qt uygulamasında ve başka
hedeflerde yeniden kullanılabilir. Donanıma yalnızca sürücü katmanı (`Led`, `Uart`; `App/Drivers/`'a taşınması planlanıyor) dokunur.
Bu, AUTOSAR Classic Platform'daki Microcontroller Abstraction Layer (MCAL) fikrinin aynısıdır.

### CR-031 · 💡 · Klasik iç içe namespace

*Kod:* `namespace airsonar::lib { … }` yerine `namespace airsonar { namespace lib { … } }`.
*Gerekçe:* Kısa yazım yalnızca C++17'de vardır. Klasik yazım C++14'te de geçerlidir; bu yüzden D-002 kaydı gerekmez.

### CR-032 · 💡 · HAL tek bir yerden çağrılıyor

*Kod:* `write(data)`, `write(data, N)` sonucunu döndürür.
*Gerekçe:* `HAL_UART_Transmit`'i yalnızca tek bir fonksiyon çağırır; aralık denetimi ve hata yönetimi tek bir yerde durur.
