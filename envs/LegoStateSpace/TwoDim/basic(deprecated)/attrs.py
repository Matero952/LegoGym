from LegoSpace import *


class BrickAttrs:
    def __init__(self, constraint_set: Constraints, brick):
        self.constraint_set = constraint_set
        self.brick = brick

    def movable(self):
        return (
            True
            if (
                Constraints.in_bounds(
                    self.constraint_set, self.brick.row, self.brick.col
                )
                and Constraints.is_occupied(
                    self.constraint_set, self.brick.row, self.brick.col
                )
                and Constraints.is_removeable(
                    self.constraint_set, self.brick.row, self.brick.col
                )
            )
            else False
        )

    def stashed(self):
        return (
            True if Constraints.is_off_table(self.brick.row, self.brick.col) else False
        )

    def reload_attrs(self):
        if self.movable():
            self.brick.moveable = True
        else:
            pass
        if self.stashed():
            self.brick.moveable = True


class ActionPreconditions:
    def __init__(self, constraint_set: Constraints, action: ([int, int], [int, int])):
        # Assume action is a tuple of indexes 'x' and 'y' where we are moving one block at a certain index 'x' to location 'y'
        self.constraint_set = constraint_set
        self.action = action

    def action_will_topple_structure(self):
        test_state = self.constraint_set.world.deepcopy()
        base_bricks = []
        pick_act, place_act = self.action
        assert isinstance(pick_act, list) and isinstance(place_act, list)
        # Now simulate the action:
        test_state[pick_act[0]][pick_act[1]] = 0
        test_state[place_act[0]][place_act[1]] = 1
        stab_state = self.constraint_set.calculate_stability()
        bricks = self.constraint_set.init_blocks()
        for brick in bricks:
            if brick.row == 0:
                base_bricks.append(brick)
        if self.constraint_set.structure_will_topple(
            base_bricks, self.constraint_set.calculate_com(bricks, stab_state)
        ):
            return True
        else:
            return False
        # Simulates action. TODO: Figure out if we can apply constraints during the action simulation.
