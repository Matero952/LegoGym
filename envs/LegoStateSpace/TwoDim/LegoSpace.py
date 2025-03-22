import numpy as np
from gymnasium import Space

from envs.LegoStateSpace.TwoDim.LegoObjects import LegoObjects


class LegoSpace(LegoObjects):
    # TODO: Define Constraints
    # Define Actions
    # Define World Boundaries
    # Define Event Handling (e.g. blocks are placed in illegal positions and there needs to be a notification)
    # WILL BE IMPLEMENTED SOON
    def __init__(
        self,
        shape: tuple[int, int],
        dtype: np.dtype,
        seed: int | np.random.Generator | None = None,
    ):
        LegoObjects.__init__(self, shape)
        self.shape = shape
        self.dtype = np.dtype(dtype)
        self.seed = seed


class Actions(object):
    def __init__(self, space: Space):
        pass
    def move(self, action: np.ndarray) -> np.ndarray:
        pass
    def remove(self, action: np.ndarray) -> np.ndarray:
        #This method will be added later when agents will be given the choice to remove blocks from the table to reach
        #a certain config
        pass


class Constraints(object):
    #This is the class for the constraints of the world. Theres a bit of physics stuff.
    def __init__(self, space: Space):
        pass
