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
    def trayectories_plot(final_state):

        for body in final_state:
            body_x = []
            body_y = []
            trayectory =  body.get_trayectory()
            for coordinate_point in trayectory:
                body_x.append(coordinate_point[0])
                body_y.append(coordinate_point[1])
            plt.plot(body_x,body_y)

        plt.show()


