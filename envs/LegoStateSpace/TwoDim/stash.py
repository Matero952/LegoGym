# uh this is the file for the stash, which in this lego env is like an inventory for the agent.
# sometimes, the agent will need to actually remove blocks from the table and put them into the stash and then
# maybe take them out. The stash will operate kinda like the stack with last in first out logic


class Stash(object):
    def __init__(self, env):
        self.env = env
        self.stash = []
        # the stash directly takes in an environment object. more functionality will be added here in a sec.

    def view_stash(self):
        return self.stash

    def push(self, block):
        self.stash.append(block)
        return None

    def pop(self, block):
        popped_block = self.stash.pop()
        return popped_block if popped_block == block else None
