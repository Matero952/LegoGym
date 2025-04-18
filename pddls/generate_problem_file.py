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
    with open(out_file, "w") as f:
            f.write(f'''(define (problem LegoProblem2d)
    (:domain pleasework)
    (:objects
    r0 r1 r2 r3 r4 - row
    c0 c1 c2 c3 c4 - col
    )
    
    (:init
    {init_block}
    )
    (:goal
    (and
    {goal_block}
    )
    )
    )
''')
    # with open(out_file, "r") as f:
    #     lines = f.readlines()
    #     for idx, line in enumerate(lines):
    #         if re.search("init", line, re.IGNORECASE):
    #             lines.insert(idx + 1, "\n" + init_block + "\n")
    #             break
    # with open(out_file, "w") as f:
    #     f.writelines(lines)
    # with open(out_file, "r") as f:
    #     lines = f.readlines()
    #     for idx, line in enumerate(lines):
    #         if re.search("goal", line, re.IGNORECASE):
    #             lines.insert(idx + 1, "\n" + goal_block + "\n")
    #             break
    # with open(out_file, "w") as f:
    #     f.writelines(lines)
    # return start

def generate_string(state):
    state_str = ""
    max_row_idx, max_col_idx = np.shape(state)
    max_row_idx = max_row_idx - 1
    max_col_idx = max_col_idx -1
    for r_idx, row in enumerate(state):
        if r_idx != 0:
            state_str += f"(is_above r{r_idx} r{r_idx - 1})"
        for c_idx, col in enumerate(row):
            if col == 0:
                state_str += f"(clear r{r_idx} c{c_idx})"
                state_str += f"(not (block_at r{r_idx} c{c_idx}))"
                state_str += f"(not (moveable r{r_idx} c{c_idx}))"
                state_str += f"(not (trapped r{r_idx} c{c_idx}))"
            elif col == 1:
                state_str += f"(block_at r{r_idx} c{c_idx})"
                state_str += f"(not (clear r{r_idx} c{c_idx}))"
                if r_idx == max_row_idx:
                    state_str += f"(moveable r{r_idx} c{c_idx})"
                    state_str += f"(not (trapped r{r_idx} c{c_idx}))"
                    continue
                if state[r_idx + 1][c_idx] == 0:
                    state_str += f"(moveable r{r_idx} c{c_idx})"
                    state_str += f"(not (trapped r{r_idx} c{c_idx}))"
                elif state[r_idx + 1][c_idx] == 1:
                    state_str += f"(not (moveable r{r_idx} c{c_idx}))"
                    state_str += f"(trapped r{r_idx} c{c_idx})"
    return state_str
if __name__ == "__main__":
    generate_problem_file("pddls/LegoProblem2d.pddl", 15000)




