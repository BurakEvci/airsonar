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


// Converts a string literal to bytes without the terminating '\0'.
// Takes a C-style array reference to get the length at compile time (D-004).
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


} // namespace lib
} // namespace airsonar

#endif /* AIRSONAR_TEXT_FORMAT_HPP */
