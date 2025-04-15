#for now just limiting blocks to 5 maybe then increase incrementally
#TODO: think about if we should flatten here or no
from seeding import *
import numpy as np
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
print(generate_full_config())


