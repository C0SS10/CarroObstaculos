import time
import RPi.GPIO as GPIO

#Si se va a utilizar pines
GPIO.setmode(GPIO.BOARD)
#Si se va a utilizar tablero numerico (Control remoto)
GPIO.setmdode(GPIO.BCM)

TRIG = 4 #Segun el lugar donde se ponga el pin
ECHO = 20 #Segun el lugar donde se ponga el pin

#Estas lineas se usan para cambiar de estado [prendido, apagado]
GPIO.setup(TRIG,GPIO.OUT) #El primer parametro es el puerto 
GPIO.setup(ECHO,GPIO.IN)

#Calculando la distancia del obstaculo al carro
def identificarDistancia():
    #Ouput se usa para emitir una señal
    GPIO.output(TRIG,True)
    time.sleep(0.00001) #Empezamos el cronometro desde 0
    GPIO.output(TRIG,False)
    #Necesitamos calcular el tiempo que se tarda en mandar una señal o input
    start_time = time.time()
    stop_time = time.time()
    #Mientras que no haya señal empezamos el cronometro
    while GPIO.input(ECHO) == False:
        start = time.time()
    #Si recibimos la señal o el input paramos el cronometro
    while GPIO.input(TRIG) == True:
        end = time.time()
    #Extraemos el tiempo final que se tardó en obtener el input o señal
    sig_time = end-start
    distance = (sig_time * 8.8888)/2

    return distance