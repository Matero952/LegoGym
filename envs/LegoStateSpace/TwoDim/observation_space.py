# wrapper for state_space, valid moves in action_space, and action_constraints basically
class ObservationSpace(object):
    def __init__(self, action, state_space, action_space):
        assert isinstance(action, tuple)
        self.action = action
        self.state_space = state_space
        self.action_space = action_space
    def get_observation(self, done = False):
        #we essentially want this function to return the observations of the action,
        #so the resultant state, the resultant valid actions, and the reward, and obv the done flag

