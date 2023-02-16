import Sensor as S
import Rpi.GPIO as GPIO
import time

if __name__ == '__main__':
    try:
        while True:
            d = S.identificarDistancia()
            print(f'La distancia entre el carro y el obstaculo en cm es:' % d)
            time.sleep()
            if S.hayHueco():
                #El carro se detiene 
                pass
            
    except KeyboardInterrupt:
        print('Ha habido una interrupción')
        GPIO.cleanup()