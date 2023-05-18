import time
from GPIOUtils import (
    pin_setup,
    pin_output,
    pin_input
)


class Sensor(): pass

class UltrasonicSensor(Sensor):
    def __init__(self, pin_echo:int, pin_trigger: int):
        self.echo = pin_echo
        self.trigger = pin_trigger
        pin_setup(self.echo, 0)
        pin_setup(self.trigger, 1)

        # Let the sensor to settle
        pin_output(self.trigger,  False)
        print('Esperando a que el sensor se establezca')
        time.sleep(2)
    
    def calculate_distance(self) -> float:
        '''Calcules the distance to the obstacule.

        Return:
            distance (float): the distance to the obstacule
        '''
        start_time = 0
        stop_time = 0

        # Get the distance sensor to trigger
        print('Calculado la distancia...')
        pin_output(self.trigger, True)
        time.sleep(0.00001)
        pin_output(self.trigger, False)
    
        # Calcule the pulse duration of the trigger
        while not pin_input(self.echo): start_time = time.time()
        while pin_input(self.echo): stop_time = time.time()
        delta_time = stop_time - start_time
    
        distance = round(delta_time * 17150, 2)
        return distance

class InfraredSensor(Sensor):
    def __init__(self, pin_infr):
        self.infr = pin_infr
        pin_setup(self.infr, 0)

    def is_pothole(self):
        '''Verify if there is a  pothole nearby.

        Return:
            True (bool): if there is a pothole.
        '''
        return pin_input(self.infr)
