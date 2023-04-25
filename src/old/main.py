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
            
            if condition1: #Si hay un muro
                Movimiento.move_forward()
            elif condition2: #Si hay un hueco
                Movimiento.move_backward()
            elif condition3: #Si hay una escalera
                Movimiento.turn_left()
            else:
                Movimiento.stop()

    except KeyboardInterrupt:
        print('Ha habido una interrupción')
        GPIO.cleanup()

if __name__ == '__main__':
    main()
