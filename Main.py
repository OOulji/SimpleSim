from celestial_objects import CelestialObject
from simulation import Simulation
from universe import Universe
from dependencies import NumericalIntegration


def main():

    univ = Universe(.005,0.01)
    planet_A = CelestialObject("name1",10.0,[0.0,0.0],[0.0,0.0],[0.0,0.0])
    planet_B = CelestialObject("name2",100.0,[0.0,0.0],[0.0,1.0],[0.0,100.0])

    sim = Simulation(univ,[planet_A,planet_B],NumericalIntegration.EulerIntegrator,600.0)

    sim.run()


if __name__ == "__main__":
    main()
    
