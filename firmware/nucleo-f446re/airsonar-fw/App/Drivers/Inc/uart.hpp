#ifndef AIRSONAR_UART_HPP
#define AIRSONAR_UART_HPP

#include "stm32f4xx_hal.h"

#include <array>
#include <cstddef>
#include <cstdint>

namespace airsonar {
namespace drivers {

// Blocking UART transmitter on top of the HAL.
class Uart final {
public:
    explicit Uart(UART_HandleTypeDef& handle) noexcept;

    // Sends the first `length` bytes of data.
    // Returns false if length is larger than the array or the transfer fails.
    template <std::size_t N>
    bool write(std::array<std::uint8_t, N> const& data, std::size_t const length) noexcept
    {
        static_assert(N <= kMaxFrameSize, "HAL_UART_Transmit takes at most 65535 bytes");
        bool sent{false};
        if (length <= N) {
            sent = transmit(data.data(), static_cast<std::uint16_t>(length));
        }
        return sent;
    }

    // Sends the whole array.
    template <std::size_t N>
    bool write(std::array<std::uint8_t, N> const& data) noexcept
    {
        return write(data, N);
    }

private:
    static constexpr std::size_t kMaxFrameSize{65535U};

    bool transmit(std::uint8_t const* const data, std::uint16_t const length) noexcept;

    UART_HandleTypeDef& handle_;
};

}  // namespace drivers
}  // namespace airsonar

#endif  // AIRSONAR_UART_HPP
