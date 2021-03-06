from typing import List
import numpy as np
from universe import Universe
from celestial_objects import CelestialObject
from dependencies import NumericalIntegration
import copy
from utils import SimulationUtils as su


class Simulation:
    def __init__(
        self,
        universe: Universe,
        initial_bodies,
        integrator: NumericalIntegration.Integrator,
        time_limit: float,
    ) -> None:
        self._universe = universe
        self._time_limit = time_limit
        self._celestial_bodies = list(initial_bodies)
        self._integrator = integrator

    def run(self) -> np.array:

        new_state = copy.deepcopy(self._celestial_bodies)
        sim_time = 0.0

        while sim_time < self._time_limit:

            for i, cb1 in enumerate(self._celestial_bodies):
                acceleration = 0
                for cb2 in self._celestial_bodies:
                    if cb1 is not cb2:

                        dist = su.calculate_distance(bodies=[cb1, cb2])
                        acceleration += (
                            (
                                (self._universe.grav_constant)
                                * (cb2.get_mass())
                            )
                            / (dist ** 3)
                        ) * (cb2.get_position() - cb1.get_position())

                new_state[i].update_acceleration(acceleration)
                velocity = self._integrator.integrate(
                    self._universe.time_step, sim_time, cb1.get_velocity(), acceleration
                )
                new_state[i].update_velocity(velocity)
                position = self._integrator.integrate(
                    self._universe.time_step, sim_time, cb1.get_position(), velocity
                )
                new_state[i].update_position(position)

            self._celestial_bodies = copy.deepcopy(new_state)
            sim_time += self._universe.time_step
        final_state = self._celestial_bodies
        return final_state

    def create_planet(self, new_planet: CelestialObject) -> CelestialObject:
        self._celestial_bodies.append(new_planet)

