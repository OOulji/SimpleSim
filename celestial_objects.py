
import numpy as np

class CelestialObject():

    def __init__(self, initial_position:np.array, name:str, mass:float, initial_velocity:np.array) -> None:

        self.mass = mass
        self.position = initial_position
        self.inital_velocity = initial_velocity
        self.name = name
    
    def update_position(self, new_position) -> None:
        self.position = new_position


