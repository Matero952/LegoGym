# This file is different block objects for two dimensions at the moment.
# Blocks all have a mass for center of mass calculations, a width, and a height, as well as a row min and column min for
# defining coordinates. Further, they also have block constraints which the program will use in parallel with environment constraints
# to determine valid moves.
# All widths and heights are in indices
from typing import Optional

from envs.LegoStateSpace.TwoDim.block_constraints import BlockConstraints


class OneByOne:
    width = 0
    height = 0

    def __init__(self, block_constraints: Optional[BlockConstraints] = None):
        self._row_min = None
        self._col_min = None
        self.block_constraints = block_constraints

    @property
    def row_min(self):
        return self._row_min

    @row_min.setter
    def row_min(self, value):
        self._row_min = value

    @property
    def col_min(self):
        return self._col_min

    @col_min.setter
    def col_min(self, value):
        self._col_min = value

    def get_block_box(self):
        return (
            self.row_min,
            self.col_min,
            self.row_min + self.height,
            self.col_min + self.width,
        )


class TwoByTwo:
    width = 1
    height = 1

    def __init__(self, block_constraints: Optional[BlockConstraints] = None):
        self._row_min = None
        self._col_min = None
        self.block_constraints = block_constraints

    @property
    def row_min(self):
        return self._row_min

    @row_min.setter
    def row_min(self, value):
        self._row_min = value

    @property
    def col_min(self):
        return self._col_min

    @col_min.setter
    def col_min(self, value):
        self._col_min = value

    def get_block_box(self):
        return (
            self.row_min,
            self.col_min,
            self.row_min + self.height,
            self.col_min + self.width,
        )


class OneByTwo:
    width = 0
    height = 1

    def __init__(self, block_constraints: Optional[BlockConstraints] = None):
        self._row_min = None
        self._col_min = None
        self.block_constraints = block_constraints

    @property
    def row_min(self):
        return self._row_min

    @row_min.setter
    def row_min(self, value):
        self._row_min = value

    @property
    def col_min(self):
        return self._col_min

    @col_min.setter
    def col_min(self, value):
        self._col_min = value

    def get_block_box(self):
        return (
            self.row_min,
            self.col_min,
            self.row_min + self.height,
            self.col_min + self.width,
        )


class TwoByOne:
    width = 1
    height = 0

    def __init__(self, block_constraints: Optional[BlockConstraints] = None):
        self._row_min = None
        self._col_min = None
        self.block_constraints = block_constraints

    @property
    def row_min(self):
        return self._row_min

    @row_min.setter
    def row_min(self, value):
        self._row_min = value

    @property
    def col_min(self):
        return self._col_min

    @col_min.setter
    def col_min(self, value):
        self._col_min = value

    def get_block_box(self):
        return (
            self.row_min,
            self.col_min,
            self.row_min + self.height,
            self.col_min + self.width,
        )


class TwoByThree:

    width = 1
    height = 2

    def __init__(self, block_constraints: Optional[BlockConstraints] = None):
        self._row_min = None
        self._col_min = None
        self.block_constraints = block_constraints

    @property
    def row_min(self):
        return self._row_min

    @row_min.setter
    def row_min(self, value):
        self._row_min = value

    @property
    def col_min(self):
        return self._col_min

    @col_min.setter
    def col_min(self, value):
        self._col_min = value

    def get_block_box(self):
        return (
            self.row_min,
            self.col_min,
            self.row_min + self.height,
            self.col_min + self.width,
        )
