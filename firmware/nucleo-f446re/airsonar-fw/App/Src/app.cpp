#include  "app.hpp"
#include "led.hpp"
#include "text_format.hpp"
#include "main.h"
#include "usart.h"


#include <array>
#include <cstddef>
#include <cstdint>
#include <limits>


namespace {

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
    bool write(std::array<std::uint8_t, N> const& data, std::size_t const length) noexcept
    {
        static_assert(N <= kMaxFrameSize, "HAL_UART_Transmit takes at most 65535 bytes");
        bool sent{false};

        if (length <= N) {
        	HAL_StatusTypeDef const status{HAL_UART_Transmit(
        			&handle_, data.data(), static_cast<std::uint16_t>(length), kTimeoutMs)};
        	sent = (status == HAL_OK);
        }

        return sent;
    }
    // Sends the whole array
    template <std::size_t N>
    bool write(std::array<std::uint8_t, N> const& data) noexcept
    {
    	return write(data, N);
    }

private:
    static constexpr std::size_t kMaxFrameSize{65535U};
    static constexpr std::uint32_t kTimeoutMs{100U};
    UART_HandleTypeDef& handle_;
};

std::uint32_t next_count(std::uint32_t const count) noexcept
{
	std::uint32_t next{0U};
	if (count < std::numeric_limits<std::uint32_t>::max()) {
		next = count + 1U;
	}
	return next;
}

}

extern "C" void app_main() noexcept
{
	constexpr std::uint32_t kLedToggleIntervalMs{500U};
    constexpr auto kBootMessage{to_bytes("airsonar: boot\r\n")};
    constexpr auto kTickPrefix{to_bytes("tick ")};
    constexpr auto kLineEnd{to_bytes("\r\n")};

    airsonar::drivers::Led led{LD2_GPIO_Port, LD2_Pin};
    Uart uart{huart2};
    std::uint32_t tick_count{0U};
    std::array<std::uint8_t, airsonar::lib::kMaxDecimalDigits> digits{};

    // Diagnostic output only: a failed transmission must not stop the firmware (CR-020).
    static_cast<void>(uart.write(kBootMessage));


	while (true) {
		led.toggle();
		tick_count = next_count(tick_count);
		std::size_t const length{airsonar::lib::to_decimal(tick_count, digits)};


		static_cast<void>(uart.write(kTickPrefix));
		static_cast<void>(uart.write(digits, length));
		static_cast<void>(uart.write(kLineEnd));

		HAL_Delay(kLedToggleIntervalMs);
	}
}
