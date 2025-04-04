import numpy as np

from envs.LegoStateSpace.TwoDim.blocks import OneByOne


def get_moveable_blocks(world_rep: np.ndarray):
    assert world_rep is not None
    moveable_blocks = []
    for row in world_rep:
        for col in row:
            assert isinstance(col, OneByOne) or col == 0
            assert col.block_constraints is not None
            if col.block_constraints.is_movable():
                moveable_blocks.append(col)
            else:
                continue
    return moveable_blocks


def get_available_spots(world_rep: np.ndarray, block):
    assert world_rep is not None
    available_spots = []
    for row in world_rep:
        for col in row:
            if col == 0:
                available_spots.append(col)
            else:
                continue
    available_spots.append(block)
    # block being moved makes an available space if the agent
    # just wants to pick it up and keep it in the same space.
    return available_spots
