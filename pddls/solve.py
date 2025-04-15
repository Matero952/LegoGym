import pyperplan as pp
import subprocess
def solve_problem(domain_file, problem_file):
    solver_command = ["pyperplan", "--heuristic", "hff", "--search", 'astar', domain_file, problem_file]
    result = subprocess.run(solver_command, capture_output=True, text=True)
    print(result)

solve_problem("C:/Users/mateo/Github/mateogym/pddls/LegoDomain2d.pddl", "C:/Users/mateo/Github/mateogym/pddls/LegoProblem2d.pddl")