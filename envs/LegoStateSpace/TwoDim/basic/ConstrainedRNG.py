# Soooo um there are a lot of possible states for a 5x5 or a 10x10. However, with restrictions, this goes down by a lot.
# For example, for 5x5, there are only 7776 possible states before considering com restrictions. This script aims to find those
# remaing states.
from LegoSpace import *


def write_indexes_to_file(states, filename):
    with open(filename, "w") as file:
        for index, state in enumerate(states):
            # Write the index of the state to the file
            file.write(f"{index} = {state}\n")


# This function is rlly scuffed but im too lazy rn to fix it so <3
def generate_possible_states(world_shape: (int, int)):
    world_row, world_col = world_shape
    passed_first_check = []
    passed_second_check = []

    # Total number of possible states for a 5x5 grid (0 or 1 in each cell)
    total_states = 2 ** (world_row * world_col)
    print(f"TOTAL STATES: {total_states}")

    for i in range(total_states):
        # Convert to binary representation and reshape into a GRID_SIZE x GRID_SIZE grid
        bin_state = (
            np.array(list(f"{i:025b}")).astype(int).reshape(world_row, world_col)
        )
        print(f"{bin_state}")
        print(f"I: {i}")
        constraints = Constraints(bin_state)
        # Check if the state is valid
        valid_state = True
        for r_idx, row in enumerate(constraints.world):
            for c_idx, col in enumerate(row):
                if not constraints.is_supported(r_idx, c_idx):
                    valid_state = False
                    break
            if not valid_state:
                break
        if valid_state:
            passed_first_check.append(constraints.world)
        print(f"Passed first check: {passed_first_check}")
        print(f"Length of first check: {len(passed_first_check)}")
    write_indexes_to_file(passed_first_check, "passed_first_check.txt")

    for state in passed_first_check:
        constraints = Constraints(state)
        stab_state = constraints.calculate_stability()
        bricks = constraints.init_blocks()
        base_bricks = []
        for brick in bricks:
            if brick.row == 0:
                base_bricks.append(brick)
            else:
                continue
        com = constraints.calculate_com(bricks, stab_state)
        if constraints.structure_will_topple(base_bricks, com):
            continue
        else:
            passed_second_check.append(constraints.world)
    print(f"Count of states: {len(passed_second_check)}")
    write_indexes_to_file(passed_second_check, "passed_second_check.txt")
    return passed_second_check


generate_possible_states((5, 5))
