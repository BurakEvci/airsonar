#include "text_format.hpp"

namespace airsonar {
namespace lib {

namespace {
constexpr std::uint32_t kDecimalBase{10U};
constexpr std::uint8_t kAsciiZero{static_cast<std::uint8_t>('0')};
}  // namespace

std::size_t to_decimal(std::uint32_t value, std::array<std::uint8_t, kMaxDecimalDigits>& digits) noexcept
{
    // 1) Collect the digits in reverse order (least significant first).
    std::array<std::uint8_t, kMaxDecimalDigits> reversed{};
    std::size_t count{0U};
    std::uint32_t remaining{value};

    while ((remaining > 0U) || (count == 0U)) {
        // take the last digit of remaining
    	std::uint32_t const digit{remaining % kDecimalBase};
        // convert it to an ASCII character and store it in reversed[count]
    	reversed[count] = static_cast<std::uint8_t>(kAsciiZero + digit);
    	// increase count by one and remove the last digit from remaining
    	++count;
    	remaining = remaining / kDecimalBase;
    }

    // 2) Copy them in the correct order (most significant first).
    for (std::size_t i{0U}; i < count; ++i) {
        // digits[i] = reversed[ ? ];
    	digits[i] = reversed[count - 1U - i];
    }
    return count;
}

}  // namespace lib
}  // namespace airsonar
