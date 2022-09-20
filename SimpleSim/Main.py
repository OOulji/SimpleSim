from celestial_objects import CelestialObject
from simulation import Simulation
from universe import Universe
from dependencies import NumericalIntegration
from utils import SimulationUtils as su



def main():

    univ = Universe(0.01,1)
    planet_A = CelestialObject("name1",1000,[0.0,0.0],[0.0,0.0],[0.0,0.0])
    planet_B = CelestialObject("name2",0.000001,[0.0,0.0],[0.0,0.3],[50.0,0.0])
    planet_C = CelestialObject("name3",0.000001,[0.0,0.0],[0.0,0.05],[200.0,0.0])

    sim = Simulation(univ,[planet_A,planet_B,planet_C],NumericalIntegration.EulerIntegrator,500.0)

    t = sim.run()
    su.trayectories_plot(t)


if __name__ == "__main__":
    main()
    
