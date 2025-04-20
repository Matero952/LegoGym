def generate_prompt(start_state, end_state):
    prompt = f'''
This is a block stacking experiment where you recieve 2 states, a starting configuring and an end goal configuration.
In each 2d array, a 1 represents a block and a 0 represents a clear cell. A block is described by its row index column index.
You can only move a block(a cell filled with a 1) if there is a 0 above it. You cannot place things above the height limit, 
and the maximum shape of the state is 5 rows by 5 columns. You can only move one block at a time, and after that move, the block's
old position becomes clear and the blocks new position becomes filled. 
Write your answer like this: 'move rx cy rx1 cy1' where rx is the blocks old row index, cy is the blocks old column index, rx1
is the blocks new row index, and cy1 is the blocks new col index. If there is no move necessary to reach the goal state, please write ' '.
Given this start state:
{start_state}
What is the next best move in order to reach this end state:
{end_state}
'''
    return prompt

if __name__ == "__main__":
    from pathlib import Path
    import sys
    pddls_directory = Path.cwd() / 'pddls'
    sys.path.append(str(pddls_directory))
    from seeding import *
    config = generate_full_config()
    start_state, end_state = generate_full_config_dict(config)[10000]
    print(generate_prompt(start_state, end_state))
    