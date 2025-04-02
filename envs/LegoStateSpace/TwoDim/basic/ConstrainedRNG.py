# Soooo um there are a lot of possible states for a 5x5 or a 10x10. However, with restrictions, this goes down by a lot.
# For example, for 5x5, there are only 7776 possible states before considering com restrictions. This script aims to find those
# remaing states.
import json
import sys

sys.path.append("/home/mateo/Github/Gym-Mateo")
import numpy as np
from LegoSpace import Constraints


def yield_states(world_shape: (int, int)):
    world_row, world_col = world_shape
    total_states = 2 ** (world_row * world_col)
    for i in range(total_states):

        bin_state = (
            np.array(list(f"{i:025b}")).astype(int).reshape(world_row, world_col)
        )
        print(f"{bin_state}")
        print(f"I: {i}")
        if np.sum(bin_state) == 0:
            with open("5x5states.json", "w") as f:
                json.dump(bin_state.tolist(), f, indent=4)
        else:
            if (
                not (first_check(bin_state))
                or not (second_check(bin_state))
                or not (third_check(bin_state))
            ):
                continue
            with open("5x5states.json", "w") as f:
                json.dump(bin_state.tolist(), f, indent=4)
    return None


def first_check(state: np.ndarray):
    summa = 0
    valid = False
    if np.sum(state) != 0:
        # Checks for seed 1 which is all 0
        for i in state[0]:
            summa += i
            if not (i >= 1):
                # Needs to be at least one block in first row
                return False
            else:
                return True
    return True
    # Return true to account for seed 1


def second_check(state: np.ndarray):
    constraint_set = Constraints(state)
    # Creates constraint set object
    for r_idx, row in enumerate(constraint_set.world):
        for c_idx, col in enumerate(row):
            # Checks if every block is supported
            if not constraint_set.is_supported(r_idx, c_idx):
                return False
            # Every block must be supported
            else:
                pass
    return True
    # Returns true if every block is supported/not floating.


def third_check(state: np.ndarray):
    constraint_set = Constraints(state)
    stability_state = constraint_set.calculate_stability()
    bricks = constraint_set.init_blocks()
    base_bricks = []

    for brick in bricks:
        if brick.row == 0:
            base_bricks.append(brick)
        else:
            continue
    com = constraint_set.calculate_com(bricks, stability_state)
    if constraint_set.structure_will_topple(base_bricks, com):
        return False
    else:
        return True


yield_states((5, 5))
