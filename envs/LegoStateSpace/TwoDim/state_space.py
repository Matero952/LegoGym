import numpy as np


class StateSpace(object):
    def __init__(self, array: np.array):
        # self.state_space = array
        self.grid_size = array.shape
        self.state_space = array.flatten()
        self.shape = self.state_space.shape
        # wanted to try representing spaces as vectors idk how this will work

    def display(self):
        print(self.state_space)
        return None


space = np.array([[1, 0, 0], [1, 0, 0], [0, 0, 0]])
state_space = StateSpace(space)
state_space.display()
print(state_space.shape)
