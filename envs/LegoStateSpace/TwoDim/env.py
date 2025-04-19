# this file is for defining a lego space. It uses a numpy array to reprsent a space.
# space constraints is another class that define some world, not block specific constraints.
# structure toppling
# TODO Add pathing please <3
# TODO Add functionality where the agent doesnt exactly choose the actual min and max of a block so you just override it to
# whichever block that the coordinate position is pointing to.
from typing import Optional
import numpy as np
from parse_action import *
from pddls.seeding import *
from action_mapping import *
from get_reward import *
from generate_classic_episode import *
import random
class legoenv(object):
    def __init__(self, episode_seed, trunc_limit):
        self.episode = generate_classic_episode(episode_seed)
        self.trunc_limit = trunc_limit
        self.state = None
        self.move_count = 0
    
    def step(self, action_idx: int):
        action = generate_action_mapping()[action_idx]
        start_block, end_pos = parse_action(action)
        start_r, start_c = start_block
        end_r, end_c = end_pos
        self.state[start_r][start_c] = 0
        self.state[end_r][end_c] = 1
        self.move_count += 1
        best_move_count_left = self.episode['min_moves'] - self.move_count
        reward = get_reward(self.state, self.episode['end']['state'], 0.1, self.move_count, 
                            best_move_count_left)
        #TODO FINISH THIS FUNCTION

    def reset(self, rng: Optional[int] = None):
        if rng is not None:
            rand_seed = random.seed(rng)
        else:
            rand_seed = random.randint(0, 15876)
        self.episode = generate_classic_episode(rand_seed)
        return None


    # def step(self, action):
    #     assert self._space is not None
    #     assert self._time_step is not None
    #     start_idxs, end_idxs = parse_action(action)
    #     start_row, start_col = start_idxs
    #     end_row, end_col = end_idxs
    #     self._space[start_row][start_col] = 0
    #     self._space[end_row][end_col] = 1


# class PlanarLegoEnvironment(object):
#     def __init__(self):
#         self._space = None
#         self._space_constraints = None
#         self._blocks = None
#         self._time_step = None

#     @property
#     def space(self):
#         return self._space

#     @space.setter
#     def space(self, value: np.ndarray):
#         self._space = value
#         # space is represented with a numpy nd array

#     @property
#     def space_constraints(self):
#         return self._space_constraints

#     @space_constraints.setter
#     def space_constraints(self, value):
#         self._space_constraints = value
#         # space constraints are just an instance of the space constraints class

#     @property
#     def blocks(self):
#         return self._blocks

#     @blocks.setter
#     def blocks(self, value):
#         self._blocks = value

#     @property
#     def time_step(self):
#         return self._time_step

#     @time_step.setter
#     def time_step(self, value):
#         self._time_step = value

#     def display_human_readable_space(self):
#         assert self._space is not None
#         assert self._space_constraints is not None
#         assert self._blocks is not None
#         return np.flipud(self._space)
#         # space is usually upside down to humans so this makes it actually like human-readable

#     def step(self, action):
#         assert self._space is not None
#         assert self._space_constraints is not None
#         assert self._blocks is not None
#         assert self._time_step is not None
#         done = False

#         # Action is like this its probably a good idea to comment this bc otherwise i will lowk forget.
#         # [block unique identifier(integer), block to move (row_min, col_min), new placement (row_min_new, col_min_new)]

#         pass

#     def reset(self):
#         self.time_step = 0
#         pass

#     def render(self):
#         pass

#     def close(self):
#         pass

