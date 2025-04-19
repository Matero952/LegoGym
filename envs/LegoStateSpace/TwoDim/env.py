# this file is for defining a lego space. It uses a numpy array to reprsent a space.
# space constraints is another class that define some world, not block specific constraints.
# structure toppling
# TODO Add pathing please <3
# TODO Add functionality where the agent doesnt exactly choose the actual min and max of a block so you just override it to
# whichever block that the coordinate position is pointing to.
from pathlib import Path
import sys
pddls_directory = Path.cwd() / 'pddls'
sys.path.append(str(pddls_directory))
from typing import Optional
import numpy as np
from parse_action import *
from seeding import *
from action_mapping import *
from get_reward import *
from generate_classic_episode import *
from action_constraints import *
from action_space import *
import random
class legoenv(object):
    def __init__(self, episode_seed, trunc_limit):
        self.episode = generate_classic_episode(episode_seed, trunc_limit)
        self.trunc_limit = trunc_limit
        self.state = self.episode['start']['state']
        self.move_count = 0
        self.truncated = False
        self.terminated = False
        if self.truncated:
            print(f'EXPERIMENT TRUNCATED AT {self.move_count} MOVES')
        if self.terminated:
            print(f"EXPERIMENT COMPLETE AFTER {self.move_count} MOVES")
    
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
        new_available_actions = get_available_actions(self.state)
        if self.move_count >= self.trunc_limit:
            self.truncated = True
        if np.array_equal(self.state, self.episode['end']['state']):
            self.terminated = True
        return self.state, new_available_actions, reward, self.truncated, self.terminated


    def reset(self, rng: Optional[int] = None):
        if rng is not None:
            rand_seed = random.seed(rng)
        else:
            rand_seed = random.randint(0, 15876)
        self.episode = generate_classic_episode(rand_seed)
        return None

if __name__ == "__main__":
    experiment = legoenv(10, 200)
    move0 = experiment.step(602)
    move1 = experiment.step(493)
    move2 = experiment.step(453)
    move3 = experiment.step(88)
    move4 = experiment.step(358)
    move5 = experiment.step(218)
    move6 = experiment.step(453)
    move7 = experiment.step(333)
    move8 = experiment.step(218)
    move9 = experiment.step(88)
    move10 = experiment.step(233)
    move11 = experiment.step(203)
    move12 = experiment.step(333)
    move13 = experiment.step(113)
    move14 = experiment.step(454)
    move15 = experiment.step(118)
    print(move15)