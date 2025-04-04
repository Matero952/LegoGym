from tools import ToolBase


class MeasuringCupBase(ToolBase):
    def __init__(self, capacity):
        ToolBase.__init__(self)
        self.capacity = capacity
        self._current_amount = None
        pass

    @property
    def current_amount(self):
        return self._current_amount

    @current_amount.setter
    def current_amount(self, value):
        self._current_amount = value
