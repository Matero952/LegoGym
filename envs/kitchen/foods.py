# This class is going to define all of the different foods in the environment as well as like subclasses.
# TODO Maybe add ripeness logic
# Fruits
class FoodBase(object):
    def __init__(self):
        pass

class Apple:
    def __init__(self):
        self._needs_fridge = False
        pass


class Banana:
    def __init__(self):
        self._needs_fridge = False
        pass


class Pear:
    def __init__(self):
        self._needs_fridge = False
        pass


class Strawberry:
    def __init__(self):
        self._needs_fridge = True
        pass


class Grape:
    def __init__(self):
        self._needs_fridge = True
        pass
