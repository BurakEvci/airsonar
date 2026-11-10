# Coding Standard

## Firmware (STM32, C++17)

**Baseline:** [AUTOSAR C++14 Guidelines (R19-03)](https://www.autosar.org/) — rules marked *required* are mandatory.
These guidelines are the main source of MISRA C++:2023.

### Language subset

- No exceptions (`-fno-exceptions`)
- No RTTI (`-fno-rtti`)
- No dynamic memory after initialization (`new`, `delete`, `malloc`, `std::vector`, `std::string`)
- Prefer `std::array`, `constexpr`, `enum class`, fixed-width integer types (`std::uint16_t`)
- Shared data between ISRs and tasks must be documented and protected

### Compiler flags

```
-std=c++17 -fno-exceptions -fno-rtti -fno-threadsafe-statics
-Wall -Wextra -Wpedantic -Wconversion -Wsign-conversion -Wshadow -Werror
```

### Static analysis

- `clang-tidy` with the configuration in [`.clang-tidy`](.clang-tidy)
- Manual review for rules that tools do not check

## Host application (Qt)

**Baseline:** [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)

## Deviations

Every deviation from the baseline is recorded here with a justification.

| ID | Rule | Scope | Justification |
|---|---|---|---|
| D-001 | AUTOSAR C++14 (all) | `Drivers/`, `Core/` (STM32 HAL, CubeMX-generated code) | Vendor C code, not modified by this project |
| D-002 | C++14 baseline | Whole firmware | C++17 features used (e.g. `std::optional`, `if constexpr`); listed per use where relevant |

## Commit messages

[Conventional Commits](https://www.conventionalcommits.org/): `type(scope): summary`

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `chore` ·
Scopes: `firmware`, `gui`, `fpga`, `linux`, `python`, `docs`, `hw`

Example: `feat(firmware): add timer-triggered ADC with DMA double buffer`
