from pathlib import Path
import sys
pddls_directory = Path.cwd() / 'pddls'
sys.path.append(str(pddls_directory))
from seeding import *
from solve import *
from generate_problem_file import *
def generate_episode_plan(seed):
    episode_plan = {}
    generate_problem_file("pddls/LegoProblem2d.pddl", seed)
    solution = solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")
    sol_plan = solution.plan._actions
    plan_length = len(solution.plan._actions)
    for idx, i in enumerate(sol_plan):
        sol_plan[idx] = str(i)
        episode_plan[idx] = []
        episode_plan[idx].append(sol_plan[idx])
        episode_plan[idx].append(1)
        if idx == (plan_length - 1):
            #at the end
            episode_plan[idx].append('done')
        else:
            episode_plan[idx].append('not_done')

    # print(vars(solution.plan))
    # print(solution.plan._actions)
    # print(len(solution.plan._actions))
    print(sol_plan)
    print(plan_length)
    print(vars(type(sol_plan[0])))
    print(str(sol_plan[0]))
    print(episode_plan)


if __name__ == "__main__":
    generate_episode_plan(15000)

