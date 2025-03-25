# My LEGO space manipulates these objects and their attributes to do what it wants.
# DEFINE ALL BRICKS HERE
from sympy.categories import Object


class Brick(Object):
    mass = 1
    connectable = False

    def __init__(self, row=None, col=None):
        self._row = None
        self._col = None
        self._moveable = False
        self._stashed = False

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def moveable(self):
        return self._moveable

    @property
    def stashed(self):
        return self._stashed

    @row.setter
    def row(self, val):
        self._row = val

    @col.setter
    def col(self, val):
        self._col = val

    @moveable.setter
    def moveable(self, val):
        self._moveable = val

    @stashed.setter
    def stashed(self, val):
        self._stashed = val


class LegoEnvironmentGround(Object):
    def __init__(self, env_shape: tuple[int, int]):
        # Define ground level. Numpy is rows by columns (height by width)
        self.row = 0
        self.col = [i for i in range(env_shape[1])]
