#include "led.hpp"
namespace airsonar {
namespace drivers {

Led::Led(GPIO_TypeDef* const port, std::uint16_t const pin) noexcept
    : port_{port}, pin_{pin}
{
}

void Led::toggle() noexcept
{
    HAL_GPIO_TogglePin(port_, pin_);
}


}
}

