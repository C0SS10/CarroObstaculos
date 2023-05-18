import RPi.GPIO as GPIO

pin_mode = [GPIO.IN, GPIO.OUT]

def gpio_mode(mode:int=0):
    if mode == 0: GPIO.setmode(GPIO.BOARD) # Using physical pin numbers
    elif mode == 1: GPIO.setmode(GPIO.BCM) # Using logical pin numbers

def pin_setup(pin:int, mode:int):
    GPIO.setup(pin, pin_mode[mode])

def pin_output(pin: int, state: bool):
    GPIO.output(pin, state)

def pin_input(pin: int):
    '''Returns the input of the given Pin'''
    return GPIO.input(pin)

def clean_gpio() -> None:
    GPIO.cleanup()
    
def disable_warnings():
    GPIO.setwarnings(False)
