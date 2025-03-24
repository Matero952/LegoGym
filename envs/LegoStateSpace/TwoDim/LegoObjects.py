# My LEGO space manipulates these objects and their attributes to do what it wants.
# DEFINE ALL BRICKS HERE
from sympy.categories import Object


class Brick(Object):
    mass = 1
    connectable = False

    def __init__(self, x=None, y=None):
        self._y = None
        self._x = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, val):
        self._x = val

    @y.setter
    def y(self, val):
        self._y = val


class LegoEnvironmentGround(Object):
    def __init__(self, env_shape: tuple[int, int]):
        # Define ground level. Numpy is rows by columns (height by width)
        self.x = [i for i in range(env_shape[1])]
        self.y = 0


class LegoObjects(Brick, LegoEnvironmentGround):
    def __init__(self, env_shape: tuple[int, int]):
        Brick.__init__(self)
        LegoEnvironmentGround.__init__(self, env_shape)
