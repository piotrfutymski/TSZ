from objects import SchedulingProblem, Solution
import sys

def weryfikacja(PROBLEM):
    problem = SchedulingProblem(0)
    problem.loadFromFile("in/"+ PROBLEM)

    solution = Solution(problem.n)
    solution.loadFromFile("out/" + PROBLEM)

    res = 0
    t_m = [ 0, 0, 0, 0 ]


    for i in range(problem.n):
        t = 0
        for j in range(4):
            t = max(t_m[j], t)
            t += problem.p[i][j]
            t_m[j] = t
        e = max(0, problem.d[i] - t)
        d = max(0, t - problem.d[i])
        v = problem.a[i] * e + problem.b[i] * d
        res += v

    toPrint = str(res) + " ---> Res for " + PROBLEM + ", Res in output: " + str(solution.res)
    if(res != solution.res):
        toPrint = toPrint + " - ERROR!!!"
    else:
        toPrint = toPrint + " - Correct :)"
    print(toPrint)


weryfikacja(sys.argv[1])