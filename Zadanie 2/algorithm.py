from objects import SchedulingProblem, Solution
import time as tt
import sys

def solve(problem):
    sol = Solution(problem.n)
    sol.permutation = []
    for i in range(4):
        sol.permutation.append([])
    for i in range(0,problem.n,4):
        if(i < problem.n):
            sol.permutation[0].append(i+1)
        if(i + 1 < problem.n):
            sol.permutation[1].append(i+2)
        if(i + 2 < problem.n):
            sol.permutation[2].append(i+3)
        if(i + 3 < problem.n):
            sol.permutation[3].append(i+4)
    return sol

time = 0

def generateSoultions(file):
    problem = SchedulingProblem(0)
    problem.loadFromFile("in/"+ file)
    time_1 = tt.time() * 1000
    a = solve(problem)
    time_2 = tt.time() * 1000
    a.saveToFile("out/"+ file)
    print(str(time_2-time_1) + " - time in [ms]")
        

generateSoultions(sys.argv[1])