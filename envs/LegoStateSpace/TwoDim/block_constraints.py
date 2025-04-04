# My goal here is to run LEGO block specific constraints in parallel with environment constraints.
# Each block will have a BlockConstraints object.
from typing import Optional

import numpy as np


class BlockConstraints:
    def __init__(self, lego_world: Optional[np.ndarray] = None):
        self._block = None
        # Please note that here in this class, block is the blocks bound box, not the object.
        self.world = lego_world

    @property
    def block(self):
        return self._block

    @block.setter
    def block(self, value):
        self._block = value

    def get_block(self):
        return self._block
        # This returns the bound box.

    def is_movable(self):
        # Block is movable if there are no blocks above it
        assert self._block is not None
        assert self.world is not None
        world_row_max, world_col_max = self.world.shape
        print(f"World row max: {world_row_max}")
        world_row_max_idx = world_row_max - 1
        row_min_idx, col_min_idx, row_max_idx, col_max_idx = self.get_block()
        print(row_min_idx, col_min_idx, row_max_idx, col_max_idx)
        if row_max_idx == world_row_max_idx:
            return True
            # Block is at the top and naturally can be picked up
        else:
            col_range = range(col_min_idx, col_max_idx + 1)
            # range is exclusive i tihnk for upper
            sliced = self.world[row_max_idx + 1 :]
            for r_idx, row in enumerate(sliced):
                for c_idx, col in enumerate(row):
                    if c_idx not in col_range:
                        sliced[r_idx][c_idx] = 0
                        # Not relevant to later sum calculation if it is outside of the column width
                    else:
                        pass
            print(sliced)
            # Take a sliced piece that is the width of the block and goes from the blocks max height to the world's max height.
            # We are essentially checking if the block can be vertically removed.
            if np.sum(sliced) != 0:
                # If there is any number besides 0 (empty), there will be some obstruction and the block is not removable.
                return False
            else:
                return True

    def is_supported(self):
        # In order for a block to be fully supported its entire width must be supported
        assert self._block is not None
        assert self.world is not None
        row_min_idx, col_min_idx, row_max_idx, col_max_idx = self.get_block()
        print(row_min_idx, col_min_idx, row_max_idx, col_max_idx)
        if row_min_idx == 0:
            # on ground and there must be supported
            return True
        else:
            print(f"aa: {self.world[row_min_idx - 1][col_min_idx: col_max_idx + 1]}")
            sliced = self.world[row_min_idx - 1][col_min_idx : col_max_idx + 1]
            # end index needs to be included
            print(sliced)
            for i in sliced:
                if i == 0:
                    return False
                else:
                    pass
            return True

    def is_stashed(self):
        assert self._block is not None
        assert self.world is not None

    def is_in_bounds(self):
        # this function checks if an object is fully in bounds
        row_min_idx, col_min_idx, row_max_idx, col_max_idx = self.get_block()
        world_row_max, world_col_max = self.world.shape
        world_rows = range(0, world_row_max - 1 + 1)
        world_cols = range(0, world_col_max - 1 + 1)
        # these are naturally the shape, which means i need to subtract one, but I also need to add one because
        # range is exclusive on last.
        return (
            True
            if (row_min_idx in world_rows and row_max_idx in world_rows)
            and (col_min_idx in world_cols and col_max_idx in world_cols)
            else False
        )


if __name__ == "__main__":
    from envs.LegoStateSpace.TwoDim.blocks import OneByOne

    world = np.array([[1, 1, 1], [1, 0, 3], [1, 2, 1], [1, 0, 1]])
    block_constraints = BlockConstraints(world)
    block = OneByOne()
    block.row_min = 2
    block.col_min = 2
    block.block_constraints = block_constraints
    block_constraints.block = block.get_block_box()
    print(block_constraints.is_movable())
    print(block_constraints.is_supported())
