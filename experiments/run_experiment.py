from claude import *
from grok import *
from prompts import *
from pathlib import Path
import sys
pddls_directory = Path.cwd() / 'pddls'
envs_directory = Path.cwd() / 'envs'
sys.path.append(str(pddls_directory))
from seeding import *
from solve import *
sys.path.append(str(envs_directory))
from LegoStateSpace.TwoDim.parse_action import *

def run_experiment(experiment):