from objects import SchedulingProblem, Solution
import time as tt
import sys

def solve(problem):
    return Solution(problem.n)

time = 0

def generateSoultions(file):
    problem = SchedulingProblem(0)
    problem.loadFromFile("in/"+ file)
    time_1 = tt.time() * 1000
    a = solve(problem)
    time_2 = tt.time() * 1000
    a.saveToFile("out/"+ file)
    print(str(time_2-time_1) + " - time in [ms]")
        
