#for now just limiting blocks to 5 maybe then increase incrementally
#TODO: think about if we should flatten here or no
from seeding import *
import numpy as np

def generate_problem_file(write_file, full_config):
    for start_cfg in full_config:
        for end_cfg in full_config:
            print(start_cfg, end_cfg)



