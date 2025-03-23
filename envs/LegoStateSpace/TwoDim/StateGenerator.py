import numpy as np

from envs.LegoStateSpace.TwoDim.LegoSpace import LegoSpace


class StateGenerator(LegoSpace):
    def __init__(self, env):
        super().__init__(env, dtype=np.float16)
        #This class is a state generator for my lego space.
        #It essentially generates different numpy array "states" with the restrictions in mind,
        #and i limit it to 'x' amount of different states before I kill it because that exponent math can get big QUICK.