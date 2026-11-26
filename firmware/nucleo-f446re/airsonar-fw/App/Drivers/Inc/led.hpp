#ifndef AIRSONAR_LED_HPP
#define AIRSONAR_LED_HPP

#include "stm32f4xx_hal.h"
#include <cstdint>

namespace airsonar {
namespace drivers {

// Drives one GPIO output pin. Port and pin are given by the caller,
// so this class does not depend on board-specific pin names.
class Led final {
public:
    Led(GPIO_TypeDef* const port, std::uint16_t const pin) noexcept;
    void toggle() noexcept;

private:
    GPIO_TypeDef* const port_;
    std::uint16_t const pin_;
};

}  // namespace drivers
}  // namespace airsonar

#endif  // AIRSONAR_LED_HPP
