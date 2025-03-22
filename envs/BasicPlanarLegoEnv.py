import numpy as np
import gymnasium as gym
from gymnasium import spaces
import ast
import copy
#TODO:
# Center of Mass (CoM): (x,y)(x,y) coordinates
# Base of Support Width: How wide the foundation is
# Distance from CoM to Base Edge: How close the center of mass is to tipping
# Torque Contribution: Summed torque of all blocks
# Max Height: Tallest block’s position


class BasicPlanarLegoEnv(gym.Env):
    def __init__(self, n, m):
        super(BasicPlanarLegoEnv, self).__init__()
        self.n = n
        self.m = m
        self.grid_size = (n, m)
        self.action_space = spaces.Discrete(self.grid_size[0], self.grid_size[1])
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(self.grid_size[0], self.grid_size[1]), dtype=np.float16)
        #Create numpy array for env.
        #World is n x m cell


    def stepper(self, n_idx, m_idx):
        #Place is a list of the n index and the m index of a block
        #Insert reward function here

        pass
    def reset(self):
        pass
    def render(self):
        pass
    def close(self):
        pass

    # def reward_func(self, n_idx, m_idx) -> float:
    #     state = self.state
    #     moves = self.moves
    #     valid = 1.0
    #     supported = 3.0
    #     stability = 5.0
    #     correct = 2.0
    #     #Add functionality for pick-up, put-down, stack, unstack moves.
    #     if m_idx == 0:
    #         if state[n_idx][m_idx] == 0:
    #             return valid + supported + stability + (correct if )
    #
    #
    #     pass

    def calculate_torque_cntrb(self):
        stability_state = (self.observation_space.sample()).copy()
        print(f"Initial state: {stability_state}")
        # print(stability_state)
        # for idx, row in enumerate(stability_state):
        #     print(row)
        #     for cidx, col in enumerate(row):
        #         print(col)
        #         stability_state[idx][cidx] = 0
        # print(stability_state)
        print(f"type: {type(stability_state)}")
        for r_idx, row in enumerate(stability_state):

            for c_idx, col in enumerate(row):

                height_from_base = self.m - r_idx
                calc = (1 / (height_from_base + 1))
                stability_state[r_idx][c_idx] = calc
                print(f"Stability state: {stability_state[r_idx][c_idx]}")
        print(f"Stability state: {stability_state}")



t = BasicPlanarLegoEnv(5, 4)
t.calculate_torque_cntrb()



