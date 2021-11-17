from objects import SchedulingProblem, Solution
import sys

def weryfikacja(PROBLEM):
    problem = SchedulingProblem(0)
    problem.loadFromFile("in/"+ PROBLEM)

    solution = Solution(problem.n)
    solution.loadFromFile("out/" + PROBLEM)

    res = 0

    for machine in range(len(solution.permutation)):
        time = 0
        for i in range(len(solution.permutation[machine])):
            task_num = solution.permutation[machine][i] - 1
            time = max(time, problem.r[task_num])
            time += problem.p[task_num]/problem.b[machine]
            if(time > problem.d[task_num]):
                res += problem.w[task_num]

    toPrint = str(res) + " ---> Res for " + PROBLEM + ", Res in output: " + str(solution.res)
    if(res != solution.res):
        toPrint = toPrint + " - ERROR!!!"
    else:
        toPrint = toPrint + " - Correct :)"
    print(toPrint)


weryfikacja(sys.argv[1])