# The fridge is going to function similarly to the Lego stash as an inventory for an agent.
class Fridge(object):
    def __init__(self, env):
        self.env = env
        self.items = []

    def store(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def view(self):
        print(f"Fridge Contents: " f"{self.items}" f"Length: {len(self.items)}")
        return self.items
