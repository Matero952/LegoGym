import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader
def solve_problem(engine_name, domain_file, problem_file):

    reader = PDDLReader()
    problem = reader.parse_problem(f"pddls/{domain_file}", f"pddls/{problem_file}")
    print(problem)
    with OneshotPlanner(name=engine_name) as planner:
        result = planner.solve(problem)
        if result.status == up.engines.PlanGenerationResultStatus.SOLVED_SATISFICING:
            print("Pyperplan returned: %s" % result.plan)
        else:
            print("No plan found.")

solve_problem("fast-downward", "LegoDomain2d.pddl", "LegoProblem2d.pddl")

