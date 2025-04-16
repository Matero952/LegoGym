from pathlib import Path
import sys
pddls_directory = Path.cwd() / 'pddls'
sys.path.append(str(pddls_directory))
from seeding import *
from generate_problem_file import *
from solve import *

class episode:
    def __init__(self, seed):
        self.seed = seed
        self.full_config = generate_full_config()
        self.config_dict = generate_full_config_dict(self.full_config)
        self.episode_start_end = self.config_dict[seed]
        self.episode_start = self.episode_start_end[0]
        self.episode_end = self.episode_start_end[1]
        self.episode_length = None
    
    def get_path_length(self, engine_name):
        generate_problem_file('LegoProblem2d.pddl', self.seed)
        path_length = len(solve_problem("lpg", 'new_lego_pls_work.pddl', 'LegoProblem2d.pddl'))
        self.episode_length = path_length



if __name__ == "__main__":
    epiode = episode(1)
    print(epiode.episode_start_end)
    