#TODO Calculate the path length of the agents move and compare it with the episodes path length
#/remaining path length and compare. Maybe negative reward it if the path length difference exceeds x actions.
import numpy as np
from action_space import *
from pathlib import Path
import sys
pddls_directory = Path.cwd() / 'pddls'
sys.path.append(str(pddls_directory))
from generate_problem_file import *
from solve import *
def get_reward(state, episode_end, reward_base, move_counter, min_moves_left):
    generate_problem_file_with_state("pddls/LegoProblem2d.pddl", (state, episode_end))
    #example move = 
    solution = solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")
    agent_plan_length = len(solution.plan._actions)
    #calculates plan length of current state to episode terminal state
    #after agent performed its action
    if agent_plan_length <= min_moves_left:
        return reward_base
        #PLEASE I THINK ITS IMPOSSIBLE FOR THE AGENT_LENGTH TO BE SHORTER
        #BUT IT CAN BE EQUAL
    elif agent_plan_length > min_moves_left:
        move_difference = agent_plan_length - min_moves_left
        return reward_base * move_difference








    