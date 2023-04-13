import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Using physical pin numbers
# GPIO.setmode(GPIO.BCM) # Using BCM numbers

PIN_TRIGGER = 4
PIN_ECHO = 18
PIN_INFR = 9

# Pin Configuration
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.setup(PIN_INFR, GPIO.IN)

def distance_to_obstacule() -> float:
    """Calcules the distance to the obstacule.

    Return:
        distance (float): the distance to the obstacule
    """
    # Let the sensor to settle
    GPIO.output(PIN_TRIGGER,False)
    print('Esperando a que el sensor se establezca')
    time.sleep(2)

    # Get the distance sensor to trigger
    print('Calculado la distancia...')
    GPIO.output(PIN_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER,False)

    start_time = time.time()
    stop_time = time.time()

    # Calcule the pulse duration of the trigger
    while GPIO.input(PIN_ECHO) == False: start_time = time.time()
    while GPIO.input(PIN_TRIGGER) == True: stop_time = time.time()
    delta_time = stop_time - start_time

    distance = round(delta_time * 17150, 2)

    return distance

def pothole() -> bool:
    """Verify if there is a  pothole nearby.

    Return:
        True (bool): if there is a pothole.
    """
    return GPIO.input(PIN_INFR)
