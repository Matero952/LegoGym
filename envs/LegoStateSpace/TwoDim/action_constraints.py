import numpy as np




def get_moveable_blocks(world_rep: np.ndarray):
    assert world_rep is not None
    moveable_blocks = []
    for row in world_rep:
        for col in row:
            assert isinstance(int, col)
            assert col.block_constraints is not None
            if col.block_constraints.is_movable():
                moveable_blocks.append(col)
            else:
                continue
    return moveable_blocks

def get_moveable_spots(state_space, row_length, col_length):
    moveable_spots = []
    for idx, i  in enumerate(state_space):
        cols_above = []
        for idx2, j in enumerate(state_space[idx::row_length]):
            cols_above.append(j)
            if sum(cols_above) > 1:
                #more than the current block is above
                break
            else:
                pass
        moveable_spots.append((idx // row_length, idx % col_length))
    return moveable_spots

