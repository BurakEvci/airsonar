#ifndef AIRSONAR_TEXT_FORMAT_HPP
#define AIRSONAR_TEXT_FORMAT_HPP

#include <array>
#include <cstddef>
#include <cstdint>

namespace airsonar {
namespace lib{

constexpr std::size_t kMaxDecimalDigits{10U};


// Writes the decimal digits of value into digits, most significant first.
// Returns the number of characters written (1 to kMaxDecimalDigits).
std::size_t to_decimal(std::uint32_t value, std::array<std::uint8_t, kMaxDecimalDigits>& digits) noexcept;

} // namespace lib
} // namespace airsonar

#endif /* AIRSONAR_TEXT_FORMAT_HPP */
