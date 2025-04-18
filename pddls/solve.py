import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader
def solve_problem(engine_name, domain_file, problem_file):

    reader = PDDLReader()
    problem = reader.parse_problem(domain_file, problem_file)
    print(problem)
    with OneshotPlanner(name=engine_name) as planner:
        result = planner.solve(problem)
        print(result.status)
        if result.status == up.engines.PlanGenerationResultStatus.SOLVED_SATISFICING:
            print("Pyperplan returned: %s" % result.plan)
        else:
            print("No plan found.")
        return result
if __name__ == "__main__":
    solve_problem("fast-downward", "pddls/domain.pddl", "pddls/LegoProblem2d.pddl")

