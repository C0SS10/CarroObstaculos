import sensor
import RPi.GPIO as GPIO
import time

def main() -> None:
    try:
        while True:
            distance = sensor.distance_to_obstacule()
            print(f'La distancia entre el carro y el obstaculo en cm es: {distance}')

            if sensor.pothole():
                print("Definitivamente, Hay un hueco")
            time.sleep(1)

    except KeyboardInterrupt:
        print('Ha habido una interrupción')
        GPIO.cleanup()

if __name__ == '__main__':
    main()
