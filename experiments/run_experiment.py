from claude import *
from grok import *
from open_router import *
from prompts import *
from quotas import *
import numpy as np
import pandas as pd
import time
from pathlib import Path
import sys
pddls_directory = Path.cwd() / 'pddls'
envs_directory = Path.cwd() / 'envs'
sys.path.append(str(pddls_directory))
from seeding import *
from solve import *
from generate_problem_file import *
sys.path.append(str(envs_directory))
from LegoStateSpace.TwoDim.parse_action import *
from LegoStateSpace.TwoDim.get_reward import *

def run_experiment(experiment, suffix=""):
    if experiment.model_name not in quotas.keys():
        print(f"{experiment.model_name} isnt in our quotas list")
        return 0
    os.makedirs("./results/", exist_ok=True)
    safe_model_name = experiment.model_name.replace("/", "_").replace(":", "_")
    save_dir = os.path.join("./results/5x5", safe_model_name + f"{suffix}/")
    os.makedirs(save_dir, exist_ok=True)
    newdf_path = os.path.join(save_dir, f'{safe_model_name}{suffix}_results.csv')
    if os.path.exists(newdf_path):
        new_df = pd.read_csv(newdf_path)
    else:
        new_df = pd.DataFrame(
            columns=["seed", "next_best_move", "predicted_next_best_move"])
        print(f"Created new dataframe")
    correct = 0
    seen = 0
    config = generate_full_config()
    conf_dict = generate_full_config_dict(config)
    for seed in range(15000, 15050):
        if seed in new_df["seed"].values:
            to_check_row = new_df[new_df["seed"] == seed]
            if to_check_row.iloc[0]["next_best_move"] == to_check_row.iloc[0]["predicted_next_best_move"]:
                correct += 1
                seen += 1
            else:
                correct += 0
                seen += 1
            # if to_check_row.iloc[0]["agent_plan_length"] <= to_check_row.iloc[0]["best_plan_length"]:
            #     correct += 1
            #     seen += 1
            # elif to_check_row.iloc[0]["agent_plan_length"] > to_check_row.iloc[0]["best_plan_length"]:
            #     correct += 0
            #     seen += 1
            print(f'SKIPPING')
            continue
        start_time = time.time()
        start, end = conf_dict[seed]
        generate_problem_file_with_state('pddls/LegoProblem2d.pddl', (start, end))
        best_solution = solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")
        best_plan_length = len(best_solution.plan._actions)
        start = np.flipud(start)
        end = np.flipud(end)
        print(start, end)
        result, action_match = experiment.process_sample(start, end)
        start_block, end_cell = parse_action(action_match)
        if start_block is None or end_cell is None:
            print(f"AAAA")
            # result = {
            #     "seed": seed,
            #     "next_best_move": best_solution.plan._actions[0] if best_plan_length > 0 else ' ',
            #     "predicted_next_best_move": ' ',
            #     "best_plan_length": best_plan_length,
            #     "agent_plan_length": 0
            #     }
            if best_plan_length == 0:
                correct += 1
                seen += 1
            else:
                correct += 0
                seen += 1
            new_df = pd.concat([new_df, pd.DataFrame([[seed, best_solution.plan._actions[0] if len(best_solution.plan._actions) > 0 else ' ',
                    ' ', result]], columns=['seed', 'next_best_move', 'predicted_next_best_move', 'response'])], 
                    ignore_index=True)
            new_df.to_csv(newdf_path, index=False)
        else:
            s_r, s_c = start_block
            e_r, e_c = end_cell
            action_statement = f"move(r{s_r}, c{s_c}, r{e_r}, c{e_c})"
            # start[s_r][s_c] = 0
            # end[e_r][e_c] = 1
            # # agent_path_length = ((get_reward(start, end, 1, best_plan_length - 1)) / -1) + best_plan_length + 1
            # generate_problem_file_with_state('pddls/LegoProblem2d.pddl', (start, end))
            # agent_solution = solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")
            # try:
            #     agent_plan_length = len(agent_solution.plan._actions) + 1
            # except AttributeError:
            #     agent_plan_length = 100000000
            # if agent_plan_length <= best_plan_length:
            #     correct += 1
            #     seen += 1
            # elif agent_plan_length > best_plan_length:
            #     correct += 0
            #     seen += 1
            if action_statement == best_solution.plan._actions[0]:
                correct += 1
                seen += 1
            else:
                correct += 0
                seen += 1
            end_time = time.time()
            time_taken = end_time-start_time
            print(f"Agent: {experiment.model_name}; accuracy: {correct/seen}; correct: {correct}; seen: {seen}; seed: {seed}; time taken: {time_taken}")
            # result = {
            #         "seed": seed,
            #         "next_best_move": best_solution.plan._actions[0] if best_plan_length > 0 else ' ',
            #         "predicted_next_best_move": action_statement,
            #         "best_plan_length": best_plan_length,
            #         "agent_plan_length": agent_plan_length
            #         }
            new_df = pd.concat([new_df, pd.DataFrame(
                [[seed, best_solution.plan._actions[0] if len(best_solution.plan._actions) > 0 else ' ', 
                  action_statement, result]],
                columns=['seed', 'next_best_move', 'predicted_next_best_move', 'response'])],
                               ignore_index=True)
            # new_df.loc[len(new_df)] = result
            new_df.to_csv(newdf_path, index=False)
            time.sleep(quotas[f'{experiment.model_name}'])
    new_df.to_csv(newdf_path, index=False)
    return experiment.model_name, correct/seen, correct, seen
        

        

run_experiment(or_experiment("deepseek/deepseek-r1:free", generate_prompt))
# run_experiment(ClaudeExperiment("claude-3-7-sonnet-20250219", generate_prompt))