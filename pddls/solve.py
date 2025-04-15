import up_fast_downward as fd
import subprocess
def solve_problem(domain_file, problem_file):
    command = [
    "./fast-downward.py",
    domain_file,
    problem_file,
    "--search",
    "astar(blind())"
]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

solve_problem("C:/Users/mateo/Github/mateogym/pddls/LegoDomain2d.pddl", "C:/Users/mateo/Github/mateogym/pddls/LegoProblem2d.pddl")