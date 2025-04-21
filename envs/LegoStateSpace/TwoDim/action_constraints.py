import numpy as np
from pathlib import Path
import sys
envs_directory = Path.cwd() / 'envs'
sys.path.append(str(envs_directory))
from LegoStateSpace.TwoDim.action_space import *

def get_moveable_spots(state_space, row_length, col_length):
    moveable_spots = []
    moveable_blocks = []
    for r_idx, row  in enumerate(state_space):
        for c_idx, col in enumerate(row):
            if r_idx == (row_length - 1):
                if col == 0:
                    moveable_spots.append((r_idx, c_idx))
                else:
                    moveable_blocks.append((r_idx, c_idx))
            elif state_space[r_idx + 1][c_idx] == 1:
                continue
            else:
                if col == 0:
                    moveable_spots.append((r_idx, c_idx))
                else:
                    moveable_blocks.append((r_idx, c_idx))
    print(f"len: {len(moveable_blocks)}")
    return moveable_spots, moveable_blocks

def get_available_actions(state_space):
    row_length, col_length = np.shape(state_space)
    moveable_spots, moveable_blocks = get_moveable_spots(state_space, row_length, col_length)
    action_space = ActionSpace((3, 3))
    valid_actions = []
    all_actions = action_space.get_all_actions()
    for action in all_actions:
        if action[0] in moveable_blocks and action[1] in moveable_spots:
            valid_actions.append(action)
        else:
            continue
    print(valid_actions)
    return valid_actions

if __name__ == "__main__":
    full_config = generate_full_config()
    full_config_dict = generate_full_config_dict(full_config)
    state = full_config_dict[1000][0]
    print(np.shape(state))
    print(len(get_available_actions(state)))

