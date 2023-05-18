import time
from GPIOUtils import (
    disable_warnings,
    gpio_mode,
    clean_gpio
)
from sensors import (
    InfraredSensor,
    UltrasonicSensor,
)
from movement import MotorController
from signals import Led

# Set GPIO MODE
gpio_mode(1) # Using BCM at the moment

# Disable warnings
disable_warnings()

# Pin Configuration
PIN_TRIGGER = 17    # 11
PIN_ECHO = 27       # 13
PIN_INFR = 22       # 15
PIN_MOTOR_A = 20    # 38
PIN_MOTOR_B = 21    # 40
PIN_LED_INFR = 19   # 35
PIN_LED_SONIC = 26  # 37

def main() -> None:
    sonic_sensor = UltrasonicSensor(PIN_ECHO, PIN_TRIGGER)
    infr_sensor = InfraredSensor(PIN_INFR)
    car_control = MotorController(PIN_MOTOR_A, PIN_MOTOR_B)
    infr_led = Led(PIN_LED_INFR)
    sonic_led = Led(PIN_LED_SONIC)
    
    try:
        while True:
            distance = sonic_sensor.calculate_distance()
            print(f'El obstaculo está a una distancia de {distance}cm')

            time.sleep(1)
            if distance < 20: 
                car_control.stop()
                sonic_led.turn_on()
            elif infr_sensor.is_pothole():
                print('Definitiva e Indudablemente Hay un hueco')
                car_control.stop()
                infr_led.turn_on()
            else:
                car_control.move_forward()
                infr_led.turn_off()
                sonic_led.turn_off()

    except KeyboardInterrupt: print('Ha habido una interrupción')
    finally: clean_gpio()

if __name__ == '__main__':
    main()

# For thecontrol of the Motor
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/ 
