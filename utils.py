import numpy as np
import matplotlib.pyplot as plt

class SimulationUtils():

    @staticmethod
    def get_trayectory(list_bodies):
        trajectories = []
        for bd in list_bodies:
            for dimension in list(bd.get_position()):
                trajectories.append(dimension)
        return trajectories

    @staticmethod
    def calculate_distance(bodies: list) -> float:
        a = np.array(bodies[0].get_position())
        b = np.array(bodies[1].get_position())
        dist = np.linalg.norm(a - b)
        return dist
    
    @staticmethod
    def trayectories_plot(trajectories):
        num_planets = int(trajectories.shape[1]/2)
        idx = 0
        for i in range(num_planets):
                plt.plot(trajectories[:,idx],trajectories[:,idx+1])
                idx += 2

        plt.show()


