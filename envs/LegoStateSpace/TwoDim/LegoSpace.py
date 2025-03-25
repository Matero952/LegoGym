import numpy as np

from envs.LegoStateSpace.TwoDim.LegoObjects import (
    Brick,
    LegoEnvironmentGround,
)


class Constraints(object):
    # This is the class for the constraints of the world. There's a bit of physics stuff.
    K_STABILITY = 1
    # Stability constant to multiply by in COM calc.

    def __init__(self, np_world):
        self.world = np_world
        self.env_shape = (np.max(np_world, axis=0), np.max(np_world, axis=1))

    # Checks
    def in_bounds(self, row_idx, col_idx):
        return row_idx < self.env_shape[0] and col_idx < self.env_shape[1]

    def is_occupied(self, row_idx, col_idx):
        return self.world.np_world[row_idx, col_idx] != 0

    def is_supported(self, row_idx, col_idx):
        if row_idx == 0:
            return True
        else:
            return self.world.np_world[row_idx - 1, col_idx] != 0
            # Config will be a numpy array

    def is_removeable(self, row_idx, col_idx):
        if row_idx == self.env_shape[1]:
            return True
        else:
            return True if self.world.np_world[row_idx, col_idx + 1] == 0 else False

    @staticmethod
    def is_off_table(row_idx, col_idx):
        return row_idx <= -1 and col_idx <= -1
        # Logic for when the model may need to remove blocks from the structure and
        # place them onto the table to reach a certain state.

    @staticmethod
    def structure_will_topple(base_blocks: list, com):
        col_bounds = []
        row_bounds = []
        com_x, com_y = com
        for brick in base_blocks:
            col_bounds.append(brick.col)
            row_bounds.append(brick.row)
        lower_col = min(col_bounds)
        lower_row = min(row_bounds)
        upper_col = max(col_bounds)
        upper_row = max(row_bounds)
        return not (lower_col <= com_x <= upper_col and lower_row <= com_y <= upper_row)
        # Returns False if the center of mass is within the base of support

    # Calculations
    def calculate_stability(self):
        stability_state = np.zeros(self.env_shape, dtype=np.float16)
        for r_idx, row in enumerate(stability_state):
            for c_idx, col in enumerate(row):
                stability_state[r_idx][c_idx] = (
                    1 / (r_idx + 1)
                ) * Constraints.K_STABILITY
                # Calculation that takes height from base in account as stuff closer to the bottom have more significance.
        return stability_state

    @staticmethod
    def calculate_com(bricks, stab_state: np.ndarray):
        # Method to calculate center of mass of block structure to determine if structure will collapse/topple over.
        mass_sum = 0
        col_sum = 0
        row_sum = 0
        for brick in bricks:
            assert isinstance(brick, Brick), "Brick must be a 'Brick' object"
            row = brick.row
            col = brick.col
            weight = stab_state[row][col]
            mass_sum += (weight * brick.mass) * Constraints.K_STABILITY
            col_sum += (col * weight * brick.mass) * Constraints.K_STABILITY
            row_sum += (row * weight * brick.mass) * Constraints.K_STABILITY

        com_x = col_sum / mass_sum
        com_y = row_sum / mass_sum
        return round(com_x), round(com_y)
        # Rounds because we are working with array indexes.

    # Initializations
    def init_blocks(self):
        bricks = []
        for r_idx, row in enumerate(self.world.np_world):
            for c_idx, col in enumerate(row):
                if self.world.np_world[r_idx, c_idx] != 0:
                    assert self.in_bounds(r_idx, c_idx), "Placement not in bounds"
                    assert self.is_supported(r_idx, c_idx), "Placement not in support"
                    new_brick = Brick()
                    new_brick.row = r_idx
                    new_brick.col = c_idx
                    bricks.append(new_brick)
                else:
                    continue
        return bricks

    def init_ground(self):
        ground_level = LegoEnvironmentGround(self.env_shape)
        return ground_level

    # Helpers
    @staticmethod
    def visualize_space(world):
        rotated_space = np.rot90(world, 2)
        print(f"Space Visualized: {rotated_space}")
        return rotated_space


class LegoSpace(Constraints):

    # Define Event Handling (e.g. blocks are placed in illegal positions and there needs to be a notification)
    # WILL BE IMPLEMENTED SOON
    def __init__(self, np_world):
        Constraints.__init__(self, np_world)
        self._config = np_world

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config):
        self._config = config


class Event:
    def __init__(self, message):
        self.message = message
        pass


class IllegalMove(Event):
    pass


class Topple(Event):
    pass


# Class Heirarchy
# The highest is the State
# Then is the Space, which is ONLY built on constraints and preconditions
# Then is the constraints
# Then is the preconditions
