from GPIOUtils import (
    pin_setup,
    pin_output
)

class MotorController:
    def __init__(self, pin_a:int, pin_b: int, pin_enable:int) -> None:
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.pin_enable = pin_enable

        # Set the Pins up
        pin_setup(self.pin_a, 1)
        pin_setup(self.pin_b, 1)
        pin_setup(self.pin_enable, 1)

        # Enable the motor
        pin_output(self.pin_enable, True)

        # The motor is stoped
        self.stop()

    def move_forward(self):
        '''Set the motor to move fowards.
        '''
        pin_output(self.pin_a, True)
        pin_output(self.pin_b, False)

    def move_backward(self):
        '''Set the motor to move fowards.
        '''
        pin_output(self.pin_a, False)
        pin_output(self.pin_b, True)
        
    def stop(self):
        '''Set the motor to stop.
        '''
        pin_output(self.pin_a, False)
        pin_output(self.pin_b, False)
