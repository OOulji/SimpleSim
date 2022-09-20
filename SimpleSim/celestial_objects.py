import numpy as np
from typing import List


class CelestialObject:
    def __init__(
        self,
        name: str,
        mass: float,
        initial_acceleration,
        initial_velocity,
        initial_position,
        

    ) -> None:

        self._mass = mass
        self._position = np.array(initial_position)
        self._velocity = np.array(initial_velocity)
        self._acceleration = np.array(initial_acceleration)
        self._name = name
        self._trayectory = [list(self._position)]
    
    def get_mass(self) -> float:
        return self._mass
    
    def get_position(self) -> np.array:
        return self._position
    def get_velocity(self) -> np.array:
        return self._velocity
    def get_acceleration(self) -> np.array:
        return self._acceleration
    def get_trayectory(self) -> List:
        return self._trayectory
    
    def update_position(self, new_position) -> None:
        self._position = np.array(new_position)
        self._trayectory.append(list(new_position))
    def update_velocity(self, new_velocity) -> None:
        self._velocity = np.array(new_velocity)
    def update_acceleration(self, new_acceleration) -> None:
        self._acceleration= np.array(new_acceleration)
