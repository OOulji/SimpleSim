import numpy as np

class SimulationUtils():

    def get_trayectory(self, list_bodies):
        trajectories = []
        for bd in list_bodies:
            for dimension in list(bd.get_position()):
                trajectories.append(dimension)
        return trajectories
    
    def calculate_distance(self, bodies: list) -> float:
        a = np.array(bodies[0].get_position())
        b = np.array(bodies[1].get_position())
        dist = np.linalg.norm(a - b)
        return dist