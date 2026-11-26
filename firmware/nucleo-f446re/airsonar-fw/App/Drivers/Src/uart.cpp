#include "uart.hpp"

namespace airsonar {
namespace drivers {

namespace {

constexpr std::uint32_t kTimeoutMs{100U};
}  // namespace

Uart::Uart(UART_HandleTypeDef& handle) noexcept : handle_{handle}
{
}

bool Uart::transmit(std::uint8_t const* const data, std::uint16_t const length) noexcept
{
    HAL_StatusTypeDef const status{HAL_UART_Transmit(&handle_, data, length, kTimeoutMs)};
    bool const sent{status == HAL_OK};
    return sent;
}

}  // namespace drivers
}  // namespace airsonar
