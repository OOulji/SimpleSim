import numpy as np
from abc import abstractclassmethod, ABC

# Numerical methods for integration.
# TO DO: Change to docstring
class Integrator(ABC):
    @abstractclassmethod
    def integrate(time_step, time, initial_vector, function) -> np.ndarray:
        pass


class EulerIntegrator(Integrator):
    def integrate(time_step, time, initial_vector, function) -> np.ndarray:

        result = np.zeros(initial_vector.shape)

        for idx, dimension in enumerate(initial_vector):
            result[idx] = dimension + time_step * function(time, dimension)

        return result
