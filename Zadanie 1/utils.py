import problem as prob
from os import walk, path

filenames = next(walk("in/"), (None, None, []))[2]  # [] if no file

def createDummyOutput(filename, n):
     f = open(filename, "w")
     f.write("0")
     f.write("\n")
     for i in range(n):
         f.write(str(i))
         f.write(" ")

def generateDummyOutput():
    for file in filenames:
        problem = prob.SchedulingProblem(0)
        problem.loadFromFile("in/"+ file)
        createDummyOutput("out/" + file, problem.n)


def weryfikacja(PROBLEM, v):
    problem = prob.SchedulingProblem(0)
    problem.loadFromFile("in/"+ PROBLEM)

    solution = prob.Solution(problem.n)
    solution.loadFromFile("out/" + PROBLEM)

    Lmax = -10000000
    time = 0
    for i in range(problem.n):
        time = max(time, problem.r[solution.permutation[i]])
        time += problem.p[solution.permutation[i]]
        if(time - problem.d[solution.permutation[i]] > Lmax):
            Lmax = time - problem.d[solution.permutation[i]]
        if(i != problem.n-1):
            time += problem.s[solution.permutation[i]][solution.permutation[i+1]]

    toPrint = str(Lmax) + "\t[ "+ format(v, '.5f') +" ]\t --->   Lmax for " + PROBLEM + ", Lmax in output: " + str(solution.Lmax)
    if(Lmax != solution.Lmax):
        toPrint = toPrint + " - ERROR!!!"
    else:
        toPrint = toPrint + " - Correct :)"
    print(toPrint)


