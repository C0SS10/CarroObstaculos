import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Seteando los motores
""" left_motor_enable = 13
left_motor_direction = (19, 26)
right_motor_enable = 20
right_motor_direction = (21, 16) """
# Hay que buscar los pines que nos sirven para los motores y la bateria

GPIO.setup(left_motor_enable, GPIO.OUT)
GPIO.setup(left_motor_direction, GPIO.OUT)
GPIO.setup(right_motor_enable, GPIO.OUT)
GPIO.setup(right_motor_direction, GPIO.OUT)

def move_forward():
    #   Se mueve hacia adelante
    GPIO.output(left_motor_direction[0], GPIO.HIGH)
    GPIO.output(left_motor_direction[1], GPIO.LOW)
    GPIO.output(right_motor_direction[0], GPIO.HIGH)
    GPIO.output(right_motor_direction[1], GPIO.LOW)
    GPIO.output(left_motor_enable, GPIO.HIGH)
    GPIO.output(right_motor_enable, GPIO.HIGH)

def move_backward():
    #   Se mueve hacia atras
    GPIO.output(left_motor_direction[0], GPIO.LOW)
    GPIO.output(left_motor_direction[1], GPIO.HIGH)
    GPIO.output(right_motor_direction[0], GPIO.LOW)
    GPIO.output(right_motor_direction[1], GPIO.HIGH)
    GPIO.output(left_motor_enable, GPIO.HIGH)
    GPIO.output(right_motor_enable, GPIO.HIGH)

def turn_left():
    #   Se mueve hacia la izquierda
    GPIO.output(left_motor_direction[0], GPIO.LOW)
    GPIO.output(left_motor_direction[1], GPIO.HIGH)
    GPIO.output(right_motor_direction[0], GPIO.HIGH)
    GPIO.output(right_motor_direction[1], GPIO.LOW)
    GPIO.output(left_motor_enable, GPIO.HIGH)
    GPIO.output(right_motor_enable, GPIO.HIGH)

def turn_right():
    #   Se mueve hacia la derecha
    GPIO.output(left_motor_direction[0], GPIO.HIGH)
    GPIO.output(left_motor_direction[1], GPIO.LOW)
    GPIO.output(right_motor_direction[0], GPIO.LOW)
    GPIO.output(right_motor_direction[1], GPIO.HIGH)
    GPIO.output(left_motor_enable, GPIO.HIGH)
    GPIO.output(right_motor_enable, GPIO.HIGH)

def stop():
    #   Se detiene
    GPIO.output(left_motor_enable, GPIO.LOW)
    GPIO.output(right_motor_enable, GPIO.LOW)