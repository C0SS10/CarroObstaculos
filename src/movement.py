from GPIOUtils import (
    pin_setup,
    pin_output
)

class MotorController:
    '''Class that controls the motor's movement through two pins that are used in a L298N Module.

    Args:
        pin_a (int): a number of the bcm or board pin.
        pin_b (int): a number of the bcm or board pin.
    '''
    def __init__(self, pin_a:int, pin_b: int) -> None:
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.can_move = False

        # Set the Pins up
        pin_setup(self.pin_a, 1)
        pin_setup(self.pin_b, 1)

        # The motor is stoped
        self.stop()

    def move_forward(self):
        '''Set the motor to move fowards.
        '''
        pin_output(self.pin_a, True)
        pin_output(self.pin_b, False)

    def move_backward(self):
        '''Set the motor to move backwards.
        '''
        pin_output(self.pin_a, False)
        pin_output(self.pin_b, True)
        
    def stop(self):
        '''Set the motor to stop.
        '''
        pin_output(self.pin_a, False)
        pin_output(self.pin_b, False)
