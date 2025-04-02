class SpaceConstraints:
    def __init__(self):
        self._space = None
        self._blocks = None
        self._stash = None

    @property
    def space(self):
        return self._space

    @space.setter
    def space(self, value):
        self._space = value

    @property
    def blocks(self):
        return self._blocks

    @blocks.setter
    def blocks(self, value):
        self._blocks = value

    @property
    def stash(self):
        return self._stash

    @stash.setter
    def stash(self, value):
        self._stash = value

    def get_com(self):
        assert self._space is not None
        mass_sum = 0
        m_x = 0
        m_y = 0
        for r_idx, row in enumerate(self._space):
            for c_idx, col in enumerate(row):
                if col != 0:
                    mass_sum += 1
                    # each cell has one mass
                    m_x += 1 * (c_idx + 1)
                    m_y += 1 * (r_idx + 1)
                    # added one to make sure all blocks even blocks at an index 0 have weight in the calculation
                else:
                    pass
        print(f"mass_sum: {mass_sum}")
        try:
            com_x = (m_x / mass_sum) - 1
            com_y = (m_y / mass_sum) - 1
        except ZeroDivisionError:
            com_x = 0
            com_y = 0
            pass
            # subtract one to shift the calculation back
        return com_x, com_y


if __name__ == "__main__":
    space_cont = SpaceConstraints()
    space = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    space_cont.space = space
    print(space_cont.get_com())
