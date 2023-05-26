from GPIOUtils import (
    pin_setup,
    pin_output
)
from time import sleep

class LedController:
    '''Controls the Led of the given pin, letting turning the led on or off.
    
    Args:
        pin (int): the pin wheter bcm or board that controls the Led.
    '''
    def __init__(self, pin: int) -> None:
        self.pin = pin
        self.__is_on = False
        pin_setup(self.pin, 1)

    def send_signal(self):
        '''Turns the led on for a second and then just turns it off.
        '''
        self.turn_on()
        sleep(1)
        self.turn_off()

    def turn_on(self):
        '''Turns the led on
        '''
        pin_output(self.pin, True)
        self.__is_on = True

    def turn_off(self):
        '''Turns the led off
        '''
        pin_output(self.pin, False)
        self.__is_on = False

    @property
    def is_on(self):
        '''Property that lets to know the state of the Led.

        Returns:
            boolean: returns the Led is on or off.
        '''
        return self.__is_on
