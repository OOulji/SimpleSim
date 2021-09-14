from typing import List
import numpy as np
from universe import Universe
from celestial_objects import CelestialObject
from dependencies import NumericalIntegration
import copy


class Simulation():

    def __init__(self, universe: Universe, initial_bodies, integrator:NumericalIntegration.Integrator, time_limit:float) -> None:
        self._universe = universe
        self._time_limit = time_limit
        self._celestial_bodies = list(initial_bodies)
        self._integrator = integrator

    def run(self) -> np.array:

        new_state = copy.deepcopy(self._celestial_bodies)
        sim_time= 0.0

        while sim_time < self._time_limit:

            for i, cb1 in enumerate(self._celestial_bodies):
                acceleration = cb1.get_acceleration()
                for cb2 in self._celestial_bodies:
                    if cb1 is not cb2:

                        dist= self.calculate_distance(bodies = [cb1,cb2])
                        acceleration += ((self._universe.grav_constant)*(cb1.get_mass()*cb2.get_mass())/dist**3)*(cb2.get_position()-cb1.get_position())
                
                new_state[i].update_acceleration(acceleration)
                velocity = self._integrator.integrate(self._universe.time_step,sim_time, cb1.get_velocity(), lambda t,y:(self._universe.grav_constant)*(cb1.get_mass()*cb2.get_mass())/dist**2)
                new_state[i].update_velocity(velocity)
                position = self._integrator.integrate(self._universe.time_step,sim_time, cb1.get_position(),lambda t,y: y)
                new_state[i].update_position(position)
                
            self._celestial_bodies = copy.deepcopy(new_state)
            sim_time += self._universe.time_step    

        return "Finished"

    def create_planet(self, new_planet:CelestialObject) -> CelestialObject:
        self._celestial_bodies.append(new_planet)
    
    def calculate_distance(self, bodies:list) -> float :
        a = np.array(bodies[0].get_position())
        b = np.array(bodies[1].get_position())
        dist = np.linalg.norm(a-b)
        return dist
    
    def get_starting_positions(self,list_bodies):
        trajectories = np.array([])
        for bd in list_bodies:
            np.append(trajectories,bd.get_position())
        return trajectories




        




