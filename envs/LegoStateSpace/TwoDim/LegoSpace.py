import numpy as np

from envs.LegoStateSpace.TwoDim.LegoObjects import (
    LegoObjects,
    Brick,
    LegoEnvironmentGround,
)


class LegoSpace(LegoObjects):
    # TODO: Define Constraints

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

        self.config = None
        # Block configuration

    @property
    def config(self):
        return self.config

    @config.setter
    def config(self, config):
        self.config = config


class Constraints(object):
    # This is the class for the constraints of the world. Theres a bit of physics stuff.
    K_STABILITY = 1

    # Tweakable value
    def __init__(self, env_shape, lego_space: LegoSpace):
        self.env_shape = env_shape
        self.lego_space = lego_space

    def in_bounds(self, x, y):
        return x <= self.env_shape[0] and y <= self.env_shape[1]

    def is_occupied(self, x, y):
        return self.lego_space.config[x, y] != 0

    def is_supported(self, x, y):
        if y == 0:
            return True
        else:
            return self.lego_space.config[x, y - 1] != 0
            # Config will be a numpy array

    def calculate_stability(self):
        stability_state = np.zeros(self.env_shape, dtype=self.lego_space.dtype)
        for r_idx, row in enumerate(stability_state):
            for c_idx, col in enumerate(row):
                stability_state[r_idx][c_idx] = (
                    1 / (r_idx + 1)
                ) * Constraints.K_STABILITY
                # Calculation that takes height from base in account as stuff closer to the bottom have more significance.
        return stability_state

    def init_blocks(self, st_state: np.ndarray):
        bricks = []
        for r_idx, row in enumerate(st_state):
            for c_idx, col in enumerate(row):
                if self.lego_space.config[r_idx, c_idx] != 0:
                    assert self.in_bounds(r_idx, c_idx), "Coordinates not in bounds."
                    assert self.is_supported(
                        r_idx, c_idx
                    ), "Floating blocks are not allowed."
                    new_brick = Brick()
                    new_brick.x = r_idx
                    new_brick.y = c_idx
                    bricks.append(new_brick)
                else:
                    continue
        return bricks

    def init_ground(self):
        ground_level = LegoEnvironmentGround(self.env_shape)
        return ground_level

    def calculate_com(self, st_state: np.ndarray):
        total_mass = sum(self.lego_space.mass * np.nditer(st_state))
        #TODO Finish
