from pathlib import Path
import sys
from parse_action import *
pddls_directory = Path.cwd() / 'pddls'
sys.path.append(str(pddls_directory))
from seeding import *
from solve import *
from generate_problem_file import *
from action_mapping import *
def generate_trajectory_plan(seed):
    
    '''trajectory kinda looks like this:
    {0:{state_before_action1, action1, reward1, doneflag1} 
    1:{state_after_action1butbeforeaction2, action2, reward2, doneflag2}
    2:... 3:...}
    '''
    episode_plan = {}
    generate_problem_file("pddls/LegoProblem2d.pddl", seed)
    config = generate_full_config()
    start, end = generate_full_config_dict(config)[seed]
    state = start.copy()
    print(start, end)
    solution = solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")
    sol_plan = solution.plan._actions
    plan_length = len(solution.plan._actions)
    for idx, i in enumerate(sol_plan):
        sol_plan[idx] = str(i)
        episode_plan[idx] = {}
        if idx == 0:
            episode_plan[idx]['before_action'] = start
        else:
            old_cell, new_cell = parse_action(sol_plan[idx - 1])
            print(old_cell, new_cell) 
            r_start, c_start = old_cell
            r_end, c_end = new_cell
            state[r_start][c_start] = 0
            state[r_end][c_end] = 1
            episode_plan[idx]['before_action'] = state
        episode_plan[idx]['action'] = generate_action_mapping()[sol_plan[idx]]
        episode_plan[idx]['reward'] = 1
        if idx == (plan_length - 1):
            #at the end
            episode_plan[idx]['done'] = True
        else:
            episode_plan[idx]['done'] = False
        state = state.copy()

    # print(vars(solution.plan))
    # print(solution.plan._actions)
    # print(len(solution.plan._actions))
    print(sol_plan)
    print(plan_length)
    print(vars(type(sol_plan[0])))
    print(str(sol_plan[0]))
    print(episode_plan)


if __name__ == "__main__":
    generate_trajectory_plan(15000)

