import RPi.GPIO as GPIO

pin_mode = [GPIO.IN, GPIO.OUT]

def gpio_mode(mode:int=0):
    '''Sets the mode of use of the GPIO.

    Args:
        mode (int): represents the mode of the GPIO, 0 is Board mode and 1 is BCM mode.
    '''
    if mode == 0: GPIO.setmode(GPIO.BOARD) # Using physical pin numbers
    elif mode == 1: GPIO.setmode(GPIO.BCM) # Using logical pin numbers

def pin_setup(pin:int, mode:int):
    '''Set the pin up in a given mode whether in or out mode.

    Args:
        mode (int): the mode
    '''
    GPIO.setup(pin, pin_mode[mode])

def pin_output(pin: int, state: bool):
    '''Set the given state to the pin.

    Args:
        pin (int): pin to set state.
        state (bool): state to be set.
    '''
    GPIO.output(pin, state)

def pin_input(pin: int):
    '''Returns the input of the given Pin

    Args:
        pin (int): required pin
    '''
    return GPIO.input(pin)

def clean_gpio() -> None:
    GPIO.cleanup()
    
def disable_warnings():
    GPIO.setwarnings(False)
