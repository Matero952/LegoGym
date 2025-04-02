# this file is for defining a lego space. It uses a numpy array to reprsent a space.
# space constraints is another class that define some world, not block specific constraints.
# structure toppling
# TODO Add pathing please <3
# TODO Add functionality where the agent doesnt exactly choose the actual min and max of a block so you just override it to
# whichever block that the coordinate position is pointing to.
import numpy as np

from blocks import OneByOne, TwoByTwo, OneByTwo, TwoByOne, TwoByThree

unique_identifiers = {1: OneByOne, 2: TwoByTwo, 3: OneByTwo, 4: TwoByOne, 5: TwoByThree}


class PlanarLegoEnvironment(object):
    def __init__(self):
        self._space = None
        self._space_constraints = None
        self._blocks = None
        self._time_step = None

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

    @property
    def time_step(self):
        return self._time_step

    @time_step.setter
    def time_step(self, value):
        self._time_step = value

    def display_human_readable_space(self):
        assert self._space is not None
        assert self._space_constraints is not None
        assert self._blocks is not None
        return np.flipud(self._space)
        # space is usually upside down to humans so this makes it actually like human-readable

    def step(self, action):
        assert self._space is not None
        assert self._space_constraints is not None
        assert self._blocks is not None
        assert self._time_step is not None
        done = False

        # Action is like this its probably a good idea to comment this bc otherwise i will lowk forget.
        # [block unique identifier(integer), block to move (row_min, col_min), new placement (row_min_new, col_min_new)]

        pass

    def reset(self):
        self.time_step = 0
        pass

    def render(self):
        pass

    def close(self):
        pass


def find_rough_block():
    pass
    # This method is for when the agent says a row min and col min that isnt defined so i just when the block they are
    # pointing to.
    # TODO Maybe add punishments for repeated undefined row min and col min
