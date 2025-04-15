from itertools import product
import numpy as np
def generate(total_blocks, cols, max_rows):
    valid_configs = []
    for heights in product(range(max_rows + 1), repeat=cols):
        if sum(heights) == total_blocks:
            config = []
            for col, height in enumerate(heights):
                for row in range(height):
                    config.append((row, col))
            valid_configs.append(config)
    print(len(valid_configs))
    return valid_configs

def generate_full_config():
    configs = generate(5, 5, 5)
    full_configs = []
    for cfg in configs:
        arr = np.zeros((5, 5))
        for pos in cfg:
            pos_row, pos_col = pos
            arr[pos_row][pos_col] = 1
        full_configs.append(arr)
    return full_configs

def generate_full_config_dict(full_config):
    counter = 0
    full_cfg_dict = {}
    for start_cfg in full_config:
        for end_cfg in full_config:
            full_cfg_dict[counter] = (start_cfg, end_cfg)
            counter += 1
    return full_cfg_dict


if __name__ == "main":
    print(generate(5, 5, 5))
#im not gonna lie i copy and pasted this code