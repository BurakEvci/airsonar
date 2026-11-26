#include  "app.hpp"
#include "led.hpp"
#include "text_format.hpp"
#include "main.h"
#include "usart.h"
#include "uart.hpp"


#include <array>
#include <cstddef>
#include <cstdint>
#include <limits>


namespace {

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
    constexpr auto kBootMessage{airsonar::lib::to_bytes("airsonar: boot\r\n")};
    constexpr auto kTickPrefix{airsonar::lib::to_bytes("tick ")};
    constexpr auto kLineEnd{airsonar::lib::to_bytes("\r\n")};

    airsonar::drivers::Led led{LD2_GPIO_Port, LD2_Pin};
    airsonar::drivers::Uart uart{huart2};
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
