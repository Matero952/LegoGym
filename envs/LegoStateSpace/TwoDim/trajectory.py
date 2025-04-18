from pathlib import Path
import sys
pddls_directory = Path.cwd() / 'pddls'
sys.path.append(str(pddls_directory))
from seeding import *
from generate_problem_file import *
from solve import *

class episode:
    def __init__(self, seed):
        self.seed = seed

        '''
        {1: [move 1 1 2 2, 1, 0], 2: [move 3 3 1 1, 1, 0], 2}
        '''


        # self.full_config = generate_full_config()
        # self.config_dict = generate_full_config_dict(self.full_config)
        # self.episode_start_end = self.config_dict[seed]
        # self.episode_start = self.episode_start_end[0]
        # self.episode_end = self.episode_start_end[1]
        # self.episode_length = None
    
    def get_plan(self, engine_name):
        generate_problem_file('LegoProblem2d.pddl', self.seed)
        plan = solve_problem("lpg", 'new_lego_pls_work.pddl', 'LegoProblem2d.pddl')
        plan_length = len(plan)
        return plan, plan_length
    
    def generate_episode_plan(self):
        plan, plan_length = self.get_plan('lpg')
        counter = 0
        episode_plan = {}
        for move in plan:
            episode_plan[counter] = [move, plan_length - counter, 
                                     'done' if plan_length - counter == 0 else 'not done']
            counter += 1
        return episode_plan

            





if __name__ == "__main__":
    epiode = episode(1)
    print(epiode.episode_start_end)
    