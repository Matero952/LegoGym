from pathlib import Path
import sys
pddls_directory = Path.cwd() / 'pddls'
sys.path.append(str(pddls_directory))
from seeding import *
from generate_problem_file import *
from solve import *

def generate_classic_episode(seed, timestep_limit):
    classic_episode = {}
    full_config = generate_full_config()
    start, end = generate_full_config_dict(full_config)[seed]
    generate_problem_file('pddls/LegoProblem2d.pddl', seed)
    solution = solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")
    plan_length = len(solution.plan._actions)
    classic_episode['min_moves'] = plan_length
    classic_episode['truncate'] = timestep_limit
    classic_episode['start'] = {}
    classic_episode['start']['state'] = start
    classic_episode['start']['done'] = False
    classic_episode['end'] = {}
    classic_episode['end']['state'] = end
    classic_episode['end']['done'] = True
    return classic_episode

if __name__ == "__main__":
    print(generate_classic_episode(10, 200))

    