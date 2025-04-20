def generate_prompt(start_state, end_state):
    prompt = f'''
This is a block-stacking task. You’re given two 2D arrays: a start and a goal configuration. Each array is 5×5, where 1 is a block and 0 is an empty cell. A block is located at its (row, column) index.

Rules:

You can only move a block (a 1) if there's a 0 directly above it.

You can’t stack above the height limit (5 rows).

Only one block can be moved at a time.

After moving, the old position becomes 0 and the new one becomes 1.

Format your answer like this:
move r_old c_old r_new c_new
If no move is needed, return: ' '.
{start_state}
What is the next best move to reach this end state:
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
    