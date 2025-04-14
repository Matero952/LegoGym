# wrapper for state_space, valid moves in action_space, and action_constraints basically
class ObservationSpace(object):
    def __init__(self, action, new_state, action_constraints, action_space, episode):
        assert isinstance(action, tuple)
        self.action = action
        self.new_state = new_state
        self.action_constraints = action_constraints
        self.action_space = action_space
        self.episode = episode
    def get_observation(self, done = False):
        #we essentially want this function to return the observations of the action,
        #so the resultant state, the resultant valid actions, and the reward, and obv the done flag
        return 1
    



