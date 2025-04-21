import pandas as pd
from pathlib import Path
import sys
import os
pddls_directory = Path.cwd() / 'pddls'
envs_directory = Path.cwd() / 'envs'
sys.path.append(str(pddls_directory))
from seeding import *
from solve import *
from generate_problem_file import *
sys.path.append(str(envs_directory))
from LegoStateSpace.TwoDim.parse_action import *
from LegoStateSpace.TwoDim.action_constraints import *

def reevaluate(agent, input_csv_file, tolerance, suffix = ""):
    save_dir = os.path.join("./results/", agent + f"{suffix}/")
    os.makedirs(save_dir, exist_ok=True)
    new_df_path = os.path.join(save_dir, f"{agent}" + "_reeval")
    new_df = pd.DataFrame(columns=['seed', 'best_plan_length', 'agent_plan_length', 'actual_plan_length_difference', 'tolerance', 'acceptable'])
    correct = 0
    seen = 0
    full_config = generate_full_config()
    config_dict = generate_full_config_dict(full_config)
    df = pd.read_csv(input_csv_file)
    for index, row in df.iterrows():
        start, end = config_dict[row['seed']]
        #start with best plan length calc
        generate_problem_file('pddls/LegoProblem2d.pddl', row['seed'])
        best_sol = solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")
        best_plan_length = len(best_sol.plan._actions)
        agent_move = row['predicted_next_best_move']
        if agent_move != ' ':
            possible_actions = get_available_actions(start)
            agent_action_parsed = parse_action(agent_move)
            s, e = agent_action_parsed
            if [s, e] not in possible_actions:
                correct += 0
                seen += 1
                new_df = pd.concat([new_df, pd.DataFrame([[row['seed'], 'Invalid Move', 'Invalid Move', 'Invalid Move', tolerance, 
                    'Invalid Move']], 
                    columns=['seed', 'best_plan_length', 'agent_plan_length', 'actual_plan_length_difference', 'tolerance', 'acceptable'])], 
                    ignore_index=True)
                continue
            else:
                agent_applied_state = step_agent_move(start, agent_move)
                generate_problem_file_with_state('pddls/LegoProblem2d.pddl', (agent_applied_state, end))
                agent_sol = solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")
                agent_sol_plan_length = len(agent_sol.plan._actions) + 1
                plan_length_diff = agent_sol_plan_length - best_plan_length
                if (agent_sol_plan_length - best_plan_length) - tolerance <= 0:
                    correct += 1
                    seen += 1
                else:
                    correct += 0
                    seen += 1
                new_df = pd.concat([new_df, pd.DataFrame([[row['seed'], best_plan_length, agent_sol_plan_length, plan_length_diff, tolerance, 
                        True if (agent_sol_plan_length - best_plan_length) - tolerance <= 0 else False]], 
                        columns=['seed', 'best_plan_length', 'agent_plan_length', 'actual_plan_length_difference', 'tolerance', 'acceptable'])], 
                        ignore_index=True)
                new_df.to_csv(new_df_path, index=False)
        else:
            if row['next_best_move'] == ' ':
                correct += 1
                seen += 1
                new_df = pd.concat([new_df, pd.DataFrame([[row['seed'], best_plan_length, 0, best_plan_length, tolerance, 
                    True]], 
                    columns=['seed', 'best_plan_length', 'agent_plan_length', 'actual_plan_length_difference', 'tolerance', 'acceptable'])], 
                    ignore_index=True)
            else:
                correct += 0
                seen += 1
                new_df = pd.concat([new_df, pd.DataFrame([[row['seed'], best_plan_length, 0, best_plan_length, tolerance, 
                        False]], 
                        columns=['seed', 'best_plan_length', 'agent_plan_length', 'actual_plan_length_difference', 'tolerance', 'acceptable'])], 
                        ignore_index=True)
    print(correct/seen)
    return correct/seen
        
def step_agent_move(start_state, move):
    updated_state = start_state.copy()
    start_block, end_cell = parse_action(move)
    s_r, s_c = start_block
    e_r, e_c = end_cell 
    updated_state[s_r][s_c] = 0
    updated_state[e_r][e_c] = 1
    return updated_state
reevaluate('claude-3-7-sonnet-20250219', 'results\claude-3-7-sonnet-20250219\claude-3-7-sonnet-20250219_results.csv', 3)




