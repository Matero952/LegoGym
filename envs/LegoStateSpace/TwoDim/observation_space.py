# wrapper for state_space, valid moves in action_space, and action_constraints basically
class ObservationSpace(object):
    def __init__(self, action: tuple, state_space):
        self.action = action
        self.state_space = state_space

