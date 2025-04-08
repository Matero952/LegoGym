class ActionSpace(object):
    def __init__(self, grid_shape):
        self.row, self.col = grid_shape

    def get_all_actions(self):
        actions = []
        for i in range(self.row):
            for j in range(self.col):
                for k in range(self.row):
                    for l in range(self.col):
                        actions.append([(i, j), (k, l)])
        print(len(actions))
        return actions


action_space = ActionSpace((5, 5))
print(action_space.get_all_actions())
print(6 % 3)
