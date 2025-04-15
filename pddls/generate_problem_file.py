#for now just limiting blocks to 5 maybe then increase incrementally
#TODO: think about if we should flatten here or no
from seeding import *
import numpy as np
import re as re

def generate_problem_file(out_file, seed):
    problem = generate_full_config_dict(generate_full_config())[seed]
    start, end = problem
    init_block = generate_string(start)
    goal_block = generate_string(end)
    with open(out_file, "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            if re.search("init", line, re.IGNORECASE):
                lines.insert(idx + 1, "\n" + init_block + "\n")
                break
    with open(out_file, "w") as f:
        f.writelines(lines)
    with open(out_file, "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            if re.search("goal", line, re.IGNORECASE):
                lines.insert(idx + 1, "\n" + goal_block + "\n")
                break
    with open(out_file, "w") as f:
        f.writelines(lines)
    return start

def generate_string(state):
    state_str = ""
    max_row_idx, max_col_idx = np.shape(state)
    max_row_idx = max_row_idx - 1
    max_col_idx = max_col_idx -1

    for r_idx, row in enumerate(state):
        for c_idx, col in enumerate(row):
            if col == 0:
                state_str += f" (clear r{r_idx} c{c_idx})\n"
                state_str += f" (not (occupied r{r_idx} c{c_idx}))\n"
            elif col == 1:
                state_str += f" (occupied r{r_idx} c{c_idx})\n"
                state_str += f" (not (clear r{r_idx} c{c_idx}))\n"
                if r_idx == max_row_idx:
                    continue
                elif state[r_idx + 1][c_idx] == 1:
                    state_str += f" (trapped r{r_idx} c{c_idx})\n"
    return state_str
generate_problem_file("C:/Users/mateo/Github/mateogym/pddls/LegoProblem2d.pddl", 1)
# print(generate_string(generate_problem_file("hehe.txt", 1)))



