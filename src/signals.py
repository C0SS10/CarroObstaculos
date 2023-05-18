from GPIOUtils import *
import time

class Led:
    def __init__(self, pin: int) -> None:
        self.pin = pin
        pin_setup(self.pin, 1)

    def send_signal(self):
        pin_output(self.pin, True)
        time.sleep(1)
        pin_output(self.pin, False)

    def turn_on(self):
        pin_output(self.pin, True)

    def turn_off(self):
        pin_output(self.pin, False)
