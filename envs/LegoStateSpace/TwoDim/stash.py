# uh this is the file for the stash, which in this lego env is like an inventory for the agent.
# sometimes, the agent will need to actually remove blocks from the table and put them into the stash and then
# maybe take them out. The stash will operate kinda like the stack with last in first out logic
import numpy as np


class Stash(object):
    def __init__(self, world_rep: np.ndarray):
        self.stash = []
        self.capacity = 25
        # 5x5

    def view_stash(self):
        return self.stash

    def push_stash(self, block):
        self.stash.append(block)
        return None

    def pop_stash(self, block):
        popped_block = self.stash.pop()
        return popped_block if popped_block == block else None
