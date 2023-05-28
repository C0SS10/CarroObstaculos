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
from signals import LedController
import time

# Set GPIO MODE
gpio_mode(1) # Using BCM at the moment

# Disable rapsberry's warnings
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
    infr_led = LedController(PIN_LED_INFR)
    sonic_led = LedController(PIN_LED_SONIC)
    
    try:
        while True:
            distance = sonic_sensor.calculate_distance()
            print(f'Hay un obstaculo a una distancia de {distance} cm.')

            time.sleep(1)
            if distance < 15:
                car_control.can_move = False
                if not sonic_led.is_on: sonic_led.turn_on()
            elif infr_sensor.is_pothole():
                print('Definitiva e Indudablemente hay un agujero.')
                car_control.can_move = False
                if not infr_led.is_on: infr_led.turn_on()
            else:
                car_control.can_move = True
                if sonic_led.is_on: sonic_led.turn_off()
                if infr_led.is_on: infr_led.turn_off()

            if car_control.can_move: car_control.move_forward()
            else: car_control.stop()


    except KeyboardInterrupt: print('Interrupción desde el teclado!')
    finally: clean_gpio()

if __name__ == '__main__': # Only is executed if this specific file
    main()

# Control of the Motor
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/ 
