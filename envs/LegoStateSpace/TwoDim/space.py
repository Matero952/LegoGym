# this file is for defining a lego space. It uses a numpy array to reprsent a space.
# space constraints is another class that define some world, not block specific constraints.
# structure toppling
import numpy as np


class Space:
    def __init__(self):
        self._space = None
        self._space_constraints = None
        self._blocks = None

    @property
    def space(self):
        return self._space

    @space.setter
    def space(self, value: np.ndarray):
        self._space = value
        # space is represented with a numpy nd array

    @property
    def space_constraints(self):
        return self._space_constraints

    @space_constraints.setter
    def space_constraints(self, value):
        self._space_constraints = value
        # space constraints are just an instance of the space constraints class

    @property
    def blocks(self):
        return self._blocks

    @blocks.setter
    def blocks(self, value):
        self._blocks = value

    def display_human_readable_space(self):
        assert self._space is not None
        assert self._space_constraints is not None
        assert self._blocks is not None
        return np.flipud(self._space)
        # space is usually upside down to humans so this makes it actually like human-readable
