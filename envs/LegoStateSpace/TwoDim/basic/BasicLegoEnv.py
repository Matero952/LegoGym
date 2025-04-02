from envs.LegoStateSpace.TwoDim.basic.LegoSpace import LegoSpace


class BasicPlanarLegoEnv(LegoSpace):
    def __init__(self, seed):
        LegoSpace.__init__(self, seed)
        # Seed is the start seed.

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        pass

    def close(self):
        pass
