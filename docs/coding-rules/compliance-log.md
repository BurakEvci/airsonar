# Coding Rules Compliance Log

🇹🇷 [Türkçe sürüm](compliance-log.tr.md) · Standard: [CODING_STANDARD.md](../../CODING_STANDARD.md)

Every AUTOSAR C++14 rule applied in `App/`, every design decision that affects compliance, and every use of
a deviation is recorded here. Entries are never deleted once committed; if code changes, a new entry
references the old one. Rule IDs and wording are verified against AUTOSAR C++14 Guidelines **Release 17-10**.

**Entry types:** ✅ rule applied · ⚠️ deviation used (see CODING_STANDARD.md §3) · 💡 design decision (no rule ID)

## Summary

| ID | Week | File | Type | Rule | Decision |
|---|---|---|---|---|---|
| CR-001 | 1 | `App/Inc/app.hpp`, `app.h` | ✅ | M16-2-3, A16-7-1 | Include guards instead of `#pragma once` |
| CR-002 | 1 | `App/Inc/app.hpp`, `app.h` | ✅ | A16-0-1 | Separate C and C++ headers instead of `#ifdef __cplusplus` |
| CR-003 | 1 | `App/Inc/app.hpp` | ✅ | A3-3-1 | `app_main()` declared in a header |
| CR-004 | 1 | `App/Src/app.cpp` | ✅ | A5-1-1, A7-1-2 | Named `constexpr` constant instead of literal `500` |
| CR-005 | 1 | `App/Src/app.cpp` | ✅ | M3-4-1 | Constant defined inside the function that uses it |
| CR-006 | 1 | `App/Src/app.cpp` | ✅ | M5-0-4 | Unsigned literal `500U` |
| CR-007 | 1 | `App/Src/app.cpp` | ✅ | A3-9-1 | Fixed-width integer types |
| CR-008 | 1 | `App/Src/app.cpp` | ✅ | A8-5-2 | Brace initialization |
| CR-009 | 1 | `App/Inc/app.hpp`, `App/Src/app.cpp` | ✅ | A15-4-4 | `noexcept` on non-throwing functions |
| CR-010 | 1 | `App/Src/app.cpp` | ✅ | A3-3-1, M7-3-3 | `Led` in an unnamed namespace in the `.cpp` file |
| CR-011 | 1 | `App/Src/app.cpp` | ✅ | A7-1-1 | `Led` data members are `const` |
| CR-012 | 1 | `App/Src/app.cpp` | ✅ | A12-4-2 (advisory) | `Led` is `final` |
| CR-013 | 1 | `App/Src/app.cpp` | 💡 | — | `Led::toggle()` is not `const` |
| CR-014 | 1 | `App/Inc/app.h`, `app.hpp` | 💡 | — | Two declarations of `app_main()` must be kept in sync |
| CR-015 | 1 | `App/Src/app.cpp` | ⚠️ | D-003 | `LD2_GPIO_Port`, `LD2_Pin` HAL macros used |
| CR-016 | 1 | `App/Src/app.cpp` | ✅ | M27-0-1 | No `<cstdio>` / `printf`; output through a `Uart` class |
| CR-017 | 1 | `App/Src/app.cpp` | ✅ | A5-2-3, A5-2-4 | Text converted to bytes with `to_bytes()`, no pointer casts |
| CR-018 | 1 | `App/Src/app.cpp` | ⚠️ | D-004 | `to_bytes()` takes a string literal as `char const (&)[N]` |
| CR-019 | 1 | `App/Src/app.cpp` | ✅ | A4-7-1 | `static_assert` proves the length fits in `std::uint16_t` |
| CR-020 | 1 | `App/Src/app.cpp` | ✅ | A0-1-2 | Result of `Uart::write()` discarded with `static_cast<void>` |
| CR-021 | 1 | `App/Src/app.cpp` | ✅ | A7-1-5 | `auto` only for the result of `to_bytes()` |
| CR-022 | 1 | `App/Src/app.cpp` | ✅ | A7-1-3 | cv-qualifiers on the right of typedef names |
| CR-023 | 1 | `App/Src/app.cpp` | 💡 | — | `Uart` constructor is `explicit` |
| CR-024 | 1 | `.clang-tidy` | 💡 | — | AUTOSAR A7-1-1 wins over clang-tidy's C++ Core Guidelines C.12 check |
| CR-025 | 1 | `App/Src/app.cpp` | 💡 | — | Blocking UART transmission accepted for now |
| CR-026 | 1 | `App/Lib/Inc/text_format.hpp` | ✅ | M7-3-1 | `to_decimal()` in namespace `airsonar::lib`, not in the global namespace |
| CR-027 | 1 | `App/Lib/Src/text_format.cpp` | ✅ | A6-5-3 (advisory) | `while` with `count == 0U` instead of `do … while` |
| CR-028 | 1 | `App/Src/app.cpp`, `App/Lib/Src/text_format.cpp` | ✅ | A4-7-1 | Explicit counter wrap; arithmetic ranges proven |
| CR-029 | 1 | `App/Src/app.cpp`, `App/Lib/Src/text_format.cpp` | ✅ | A5-2-5 | Array indices and lengths checked against the array size |
| CR-030 | 1 | `App/Lib/` | 💡 | — | Library layer never includes HAL / CubeMX headers |
| CR-031 | 1 | `App/Lib/` | 💡 | — | Classic nested namespaces instead of C++17 `namespace a::b` |
| CR-032 | 1 | `App/Src/app.cpp` | 💡 | — | `Uart::write(data)` delegates to `write(data, length)` |

## Week 1 — first C++ firmware (`app_main`, LED blink)

Final code reviewed in this week:

```cpp
// App/Inc/app.h  — C interface, included by Core/Src/main.c
#ifndef AIRSONAR_APP_H
#define AIRSONAR_APP_H
/* C++ declaration: app.hpp. Keep both in sync (CR-014). */
void app_main(void);
#endif
```

```cpp
// App/Inc/app.hpp — C++ declaration, included by App/Src/app.cpp
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

### CR-001 · M16-2-3, A16-7-1 · Include guards instead of `#pragma once`

*Rules:* Include guards shall be provided (M16-2-3). The `#pragma` directive shall not be used (A16-7-1).
*Before:* `#pragma once`
*After:* `#ifndef AIRSONAR_APP_HPP` / `#define AIRSONAR_APP_HPP` / `#endif`
*Why:* `#pragma` behaviour is implementation-defined. Include guards are standard C++ and work with every
compiler. Guard names start with the project name to avoid collisions.

### CR-002 · A16-0-1 · Separate C and C++ headers

*Rule:* The pre-processor shall only be used for unconditional and conditional file inclusion and include
guards, and using a fixed list of directives. The rule's own example marks a declaration inside `#ifdef`
as non-compliant.
*Before:* one header with `#ifdef __cplusplus extern "C" { ... } #endif` around the declaration.
*After:* two headers: `app.h` (plain C, for `main.c`) and `app.hpp` (C++, `extern "C" ... noexcept`).
*Why:* The common single-header pattern uses conditional compilation for a declaration, not for file
inclusion. Two headers keep every preprocessor use limited to include guards. It also allows the C++
declaration to carry `noexcept` (CR-009), which is not valid C. See CR-014 for the cost of this choice.

### CR-003 · A3-3-1 · `app_main()` declared in a header

*Rule:* Objects or functions with external linkage (including members of named namespaces) shall be
declared in a header file.
*After:* `app_main()` is declared in `app.hpp` and defined in `app.cpp` with C linkage, so the C file
`main.c` can call it without C++ name mangling.
*Why:* One declaration in a header makes the definition and every C++ caller agree on the signature.

### CR-004 · A5-1-1, A7-1-2 · Named constant instead of a literal

*Rules:* Literal values shall not be used apart from type initialization, otherwise symbolic names shall be
used instead (A5-1-1). The `constexpr` specifier shall be used for values that can be determined at compile time (A7-1-2).
*Before:* `HAL_Delay(500);`
*After:* `constexpr std::uint32_t kLedToggleIntervalMs{500U};` then `HAL_Delay(kLedToggleIntervalMs);`
*Why:* The name states what the number means and its unit (ms).

### CR-005 · M3-4-1 · Constant defined where it is used

*Rule:* An identifier declared to be an object or type shall be defined in a block that minimizes its visibility.
*Before (first draft):* `kLedToggleIntervalMs` at namespace scope.
*After:* defined inside `app_main()`, the only function that uses it.
*Why:* The smaller the scope, the fewer places can depend on or misuse the identifier.

### CR-006 · M5-0-4 · Unsigned literal `500U`

*Rule:* An implicit integral conversion shall not change the signedness of the underlying type.
*Before:* `500` (`int`, signed) initializing a `std::uint32_t`.
*After:* `500U` (`unsigned int`).
*Why:* No implicit signed-to-unsigned conversion takes place.

### CR-007 · A3-9-1 · Fixed-width integer types

*Rule:* Fixed width integer types from `<cstdint>`, indicating the size and signedness, shall be used in
place of the basic numerical types.
*After:* `std::uint32_t` for the delay, `std::uint16_t` for the pin mask.
*Why:* The size of `int` depends on the platform; on a microcontroller register widths matter.
`std::uint16_t` matches the HAL pin type.

### CR-008 · A8-5-2 · Brace initialization

*Rule:* Braced-initialization `{}`, without equals sign, shall be used for variable initialization.
*After:* `kLedToggleIntervalMs{500U}`, `port_{port}`, `pin_{pin}`, `Led led{LD2_GPIO_Port, LD2_Pin};`
*Why:* Brace initialization rejects narrowing conversions at compile time and has one syntax for all types.

### CR-009 · A15-4-4 · `noexcept` on non-throwing functions

*Rule:* A declaration of non-throwing function shall contain noexcept specification.
*After:* the `Led` constructor, `Led::toggle()` and `app_main()` are `noexcept`.
*Why:* The firmware is built with `-fno-exceptions`, so nothing can throw. `noexcept` documents this and
enables optimizations. `app_main()` can carry `noexcept` only in the C++ header (CR-002).

### CR-010 · A3-3-1, M7-3-3 · Helper class in an unnamed namespace

*Rules:* A3-3-1 (above). There shall be no unnamed namespaces in header files (M7-3-3).
*After:* `Led` is defined inside `namespace { ... }` in `app.cpp`.
*Why:* `Led` is used only in `app.cpp`. The unnamed namespace gives it internal linkage, so it needs no
header declaration and cannot collide with names in other files. Unnamed namespaces are forbidden only in headers.

### CR-011 · A7-1-1 · `const` data members

*Rule:* Constexpr or const specifiers shall be used for immutable data declaration.
*Before (first draft):* `GPIO_TypeDef* port_;` and `std::uint16_t pin_;`
*After:* `GPIO_TypeDef* const port_;` and `std::uint16_t const pin_;`
*Why:* A `Led` is bound to one pin for its whole life; the members never change after construction.
`const` makes the compiler enforce this. Side effect: `Led` objects cannot be copy-assigned, which is intended.

### CR-012 · A12-4-2 (advisory) · `Led` is `final`

*Rule:* If a public destructor of a class is non-virtual, then the class should be declared final.
*After:* `class Led final`
*Why:* `Led` has an implicit, non-virtual destructor and is not designed as a base class. Deleting a derived
object through a base pointer would be undefined behaviour; `final` rules out inheritance altogether.

### CR-013 · 💡 · `Led::toggle()` is not `const`

*Before (first draft):* `void toggle() const noexcept`
*After:* `void toggle() noexcept`
*Why:* No rule forbids the first version, and the compiler accepts it because no data member changes.
But the function changes the state of the hardware the object represents. Marking it `const` would tell
readers that calling it has no visible effect, which is false (*logical constness*).

### CR-014 · 💡 · Two declarations of `app_main()`

*Decision:* CR-002 introduces two declarations of the same function: `void app_main(void);` in `app.h`
(compiled as C) and `extern "C" void app_main() noexcept;` in `app.hpp` (compiled as C++).
*Risk:* the C and C++ compilers never see each other's declaration, and the linker matches C functions by
name only. A mismatch would not be detected at build time.
*Mitigation:* the signature takes no arguments and returns nothing, so there is nothing to mismatch. Both
headers carry a comment pointing to the other. Any future change to the signature must update both files
in the same commit.

### CR-015 · ⚠️ D-003 · HAL macros `LD2_GPIO_Port`, `LD2_Pin`

*Rules affected:* Traditional C-style casts shall not be used (A5-2-2). An object with integer type or
pointer to void type shall not be converted to an object with pointer type (M5-2-8).
*Code:* `Led led{LD2_GPIO_Port, LD2_Pin};`
*Why the deviation:* CubeMX generates `#define LD2_GPIO_Port GPIOA`; CMSIS defines `GPIOA` as
`((GPIO_TypeDef *) GPIOA_BASE)`, a C-style cast from an integer address to a pointer. This is how
memory-mapped registers are reached through the vendor headers.
*Containment:* the macros are used only where a `Led` is constructed. The rest of the code uses the typed
`GPIO_TypeDef*` and `std::uint16_t` values stored in the object.

### UART output (CR-016 … CR-025)

```cpp
// App/Src/app.cpp (additions)
#include "usart.h"
#include <array>
#include <cstddef>

// Converts a string literal to its bytes, without the terminating '\0'.
template <std::size_t N>
constexpr std::array<std::uint8_t, N - 1U> to_bytes(char const (&text)[N]) noexcept
{
    static_assert(N > 1U, "Text must not be empty");
    std::array<std::uint8_t, N - 1U> bytes{};
    for (std::size_t i{0U}; i < (N - 1U); ++i) {
        bytes[i] = static_cast<std::uint8_t>(text[i]);
    }
    return bytes;
}

class Uart final {
public:
    explicit Uart(UART_HandleTypeDef& handle) noexcept : handle_{handle} {}

    template <std::size_t N>
    bool write(std::array<std::uint8_t, N> const& data) noexcept
    {
        static_assert(N <= kMaxFrameSize, "HAL_UART_Transmit takes at most 65535 bytes");
        HAL_StatusTypeDef const status{
            HAL_UART_Transmit(&handle_, data.data(), static_cast<std::uint16_t>(N), kTimeoutMs)};
        return status == HAL_OK;
    }

private:
    static constexpr std::size_t kMaxFrameSize{65535U};
    static constexpr std::uint32_t kTimeoutMs{100U};
    UART_HandleTypeDef& handle_;
};
```

### CR-016 · M27-0-1 · No `<cstdio>`

*Rule:* The stream input/output library `<cstdio>` shall not be used.
*Decision:* no `printf`. Text is sent with `HAL_UART_Transmit` through a small `Uart` class.
*Why:* `printf` has no type checking of its arguments (format string bugs), uses a variadic interface, and on
a microcontroller pulls in a large formatting library and often dynamic memory.

### CR-017 · A5-2-3, A5-2-4 · Text to bytes without pointer casts

*Rules:* A cast shall not remove any const or volatile qualification from the type of a pointer or reference
(A5-2-3). `reinterpret_cast` shall not be used (A5-2-4).
*Problem:* `HAL_UART_Transmit` takes `const uint8_t*`, a string literal is `const char[]`. The usual
`(uint8_t*)"text"` is a C-style cast, `reinterpret_cast<const uint8_t*>` is forbidden by A5-2-4.
*After:* `constexpr` function `to_bytes()` copies each character with a `static_cast<std::uint8_t>` into a
`std::array<std::uint8_t, N - 1>` at compile time. No pointer is cast; the array's `data()` already has the right type.
*Bonus:* the conversion happens at compile time, so it costs nothing at run time.

### CR-018 · ⚠️ D-004 · String literal parameter

*Rule affected:* C-style arrays should not be used (A18-1-1, advisory).
*Code:* `to_bytes(char const (&text)[N])`
*Why:* a string literal *is* a C-style array. Taking it by reference to an array is the only way to receive
its length `N` at compile time. The array is only read inside `to_bytes()`; everything else uses `std::array`.

### CR-019 · A4-7-1 · Length fits in `std::uint16_t`

*Rule:* An integer expression shall not lead to data loss.
*Code:* `static_assert(N <= kMaxFrameSize, ...)` followed by `static_cast<std::uint16_t>(N)`.
*Why:* `HAL_UART_Transmit` takes the length as `uint16_t`. The `static_assert` proves at compile time that
`N` fits, so the cast can never lose data. A message longer than 65 535 bytes fails to compile.

### CR-020 · A0-1-2 · Return value discarded explicitly

*Rule:* The value returned by a function having a non-void return type that is not an overloaded operator
shall be used. The rule allows discarding with `static_cast<void>`.
*Code:* `static_cast<void>(uart.write(kTickMessage));`
*Why:* this output is diagnostic only. A failed transmission must not stop the firmware, so the result is
intentionally ignored, and the cast makes this decision visible in the code.

### CR-021 · A7-1-5 · `auto` for a function result

*Rule:* `auto` shall only be used in listed cases, including (1) a variable with the same type as the return
type of a function call.
*Code:* `constexpr auto kBootMessage{to_bytes("airsonar: boot\r\n")};`
*Why:* the type is `std::array<std::uint8_t, 16>`. Writing the length by hand would have to be updated every
time the text changes; `auto` takes it from `to_bytes()`.

### CR-022 · A7-1-3 · cv-qualifiers on the right

*Rule:* CV-qualifiers shall be placed on the right hand side of the type that is a typedef or a using name.
*Code:* `std::uint16_t const pin`, `std::array<...> const& data`, `HAL_StatusTypeDef const status`.
*Why:* `std::uint16_t` and `HAL_StatusTypeDef` are typedef names. Writing `const` on the right reads
consistently from right to left and avoids the classic misreading of `const` with pointer typedefs.

### CR-023 · 💡 · `explicit` constructor

*Code:* `explicit Uart(UART_HandleTypeDef& handle) noexcept`
*Why:* A12-1-4 requires `explicit` only for single-argument constructors of *fundamental* type, which
`UART_HandleTypeDef&` is not. `explicit` is still used (C++ Core Guidelines C.46) so a `UART_HandleTypeDef`
cannot silently turn into a `Uart` object.

### CR-024 · 💡 · Tool conflict: AUTOSAR A7-1-1 vs C++ Core Guidelines C.12

*Finding:* clang-tidy's `cppcoreguidelines-avoid-const-or-ref-data-members` (C.12: "don't make data members
const or references") warns about `Led::port_`, `Led::pin_` and `Uart::handle_`.
*Decision:* the firmware baseline is AUTOSAR C++14 (CODING_STANDARD.md §1.1). A7-1-1 asks for `const` on
immutable data (CR-011), and these objects are intentionally not copy-assignable. The check is disabled in
`.clang-tidy` for the firmware.
*Lesson:* coding standards can contradict each other. The project picks one baseline and records the conflict.

### CR-025 · 💡 · Blocking transmission

*Decision:* `HAL_UART_Transmit` blocks the CPU until all bytes are sent.
*Cost:* at 115 200 baud one byte takes 10 bits / 115 200 ≈ 87 µs. The 16-byte boot message blocks ≈ 1.4 ms,
the 6-byte tick message ≈ 0.5 ms every 500 ms.
*Why acceptable now:* nothing else runs yet. Week 3 moves transmission to DMA, when sampling must not be delayed.

### Tick counter and `to_decimal()` (CR-026 … CR-032)

```cpp
// App/Lib/Src/text_format.cpp
std::size_t to_decimal(std::uint32_t value, std::array<std::uint8_t, kMaxDecimalDigits>& digits) noexcept
{
    std::array<std::uint8_t, kMaxDecimalDigits> reversed{};
    std::size_t count{0U};
    std::uint32_t remaining{value};

    while ((remaining > 0U) || (count == 0U)) {
        std::uint32_t const digit{remaining % kDecimalBase};
        reversed[count] = static_cast<std::uint8_t>(kAsciiZero + digit);
        ++count;
        remaining = remaining / kDecimalBase;
    }
    for (std::size_t i{0U}; i < count; ++i) {
        digits[i] = reversed[count - 1U - i];
    }
    return count;
}
```

Tested on the host with strict flags: 0, 7, 10, 42, 472, 1000 and 4 294 967 295 all convert correctly.

### CR-026 · M7-3-1 · No functions in the global namespace

*Rule:* The global namespace shall only contain `main`, namespace declarations and `extern "C"` declarations.
*After:* `to_decimal()` and `kMaxDecimalDigits` live in `namespace airsonar { namespace lib { … } }`.
*Why:* names in the global namespace can collide with any library, including the HAL's C functions.

### CR-027 · A6-5-3 (advisory) · No `do` statement

*Rule:* Do statements should not be used.
*Code:* `while ((remaining > 0U) || (count == 0U))`
*Why:* converting 0 needs the loop body to run at least once, the classic use case of `do … while`. The
extra condition `count == 0U` gives the same guarantee with a plain `while`, whose condition is visible at the top.

### CR-028 · A4-7-1 · No data loss in integer expressions

*Rule:* An integer expression shall not lead to data loss. The rule explicitly includes wrap-around.
*Cases:*
- `++tick_count` would wrap from 4 294 967 295 to 0. `next_count()` makes the wrap explicit with a range check:
  ```cpp
  std::uint32_t next_count(std::uint32_t const count) noexcept
  {
      std::uint32_t next{0U};
      if (count < std::numeric_limits<std::uint32_t>::max()) {
          next = count + 1U;
      }
      return next;
  }
  ```
  At one tick every 500 ms the wrap happens after ≈ 68 years; the guard documents the behaviour rather than relying on it never happening.
- `static_cast<std::uint8_t>(kAsciiZero + digit)`: `digit` is `remaining % 10`, so 0–9; the result is 48–57 and fits in `std::uint8_t`.
- `count - 1U - i`: the loop runs only while `i < count`, so the result is at least 0 and never wraps.

### CR-029 · A5-2-5 · No access beyond an array's range

*Rule:* An array shall not be accessed beyond its range.
*Cases:*
- `Uart::write(data, length)` checks `length <= N` before calling the HAL and returns `false` otherwise.
- In `to_decimal()`, `count` can reach at most 10, because a `std::uint32_t` has at most 10 decimal digits, which equals `kMaxDecimalDigits`.
*Observed in practice:* while learning, the index `count - 1U - 1` was tried instead of `count - 1U - i`. For a
one-digit number this evaluates to `SIZE_MAX` and reads memory outside the array; the test printed random
characters (`"O"`, `"U"`). This is exactly the class of defect A5-2-5 targets, and it only shows up for specific inputs.

### CR-030 · 💡 · Library layer without hardware dependencies

*Decision:* code in `App/Lib/` includes only standard headers and never `main.h`, `usart.h` or any HAL header.
*Why:* library code can then be compiled and unit-tested on a PC, and reused in the Qt application and other
targets. Only the driver layer (`Led`, `Uart`, planned to move to `App/Drivers/`) touches the hardware.
This is the same idea as the AUTOSAR Classic Platform's Microcontroller Abstraction Layer (MCAL).

### CR-031 · 💡 · Classic nested namespaces

*Code:* `namespace airsonar { namespace lib { … } }` instead of `namespace airsonar::lib { … }`.
*Why:* the short form is C++17-only. The classic form is valid C++14, so no D-002 entry is needed.

### CR-032 · 💡 · One place calls the HAL

*Code:* `write(data)` returns `write(data, N)`.
*Why:* only one function calls `HAL_UART_Transmit`, so range checks and error handling live in one place.
