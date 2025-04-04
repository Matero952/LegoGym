from envs.LegoStateSpace.TwoDim.blocks import OneByOne


class SpaceConstraints:
    def __init__(self):
        self._space = None
        self._stash = None

    @property
    def space(self):
        return self._space

    @space.setter
    def space(self, value):
        self._space = value

    @property
    def stash(self):
        return self._stash

    @stash.setter
    def stash(self, value):
        self._stash = value

    def is_valid_state(self):
        assert self._space is not None
        for row in self._space:
            for col in row:
                assert isinstance(col, OneByOne) or col == 0
                if col != 0:
                    if col.block_constraints.is_supported():
                        continue
                    else:
                        return False


if __name__ == "__main__":
    space_cont = SpaceConstraints()
    space = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    space_cont.space = space
    print(space_cont.get_com())
