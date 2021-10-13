import problem as prob

PROBLEM = "141216_25.txt"


solution = prob.Solution()
solution.loadFromFile("out/" + PROBLEM)

problem = prob.SchedulingProblem(0)
problem.loadFromFile("in/"+ PROBLEM)

Lmax = -10000000
time = 0
for i in range(problem.n):
    time = max(time, problem.r[solution.permutation[i]])
    time += problem.p[solution.permutation[i]]
    if(time - problem.d[solution.permutation[i]] > Lmax):
        Lmax = time - problem.d[solution.permutation[i]]
    if(i != problem.n-1):
        time += problem.s[solution.permutation[i]][solution.permutation[i+1]]

print("Lmax for " + PROBLEM + " = " + str(Lmax))
print("Lmax in output, for " + PROBLEM + " = " + str(solution.Lmax))
if(Lmax != solution.Lmax):
    print("ERROR!!!")
else:
    print("Correct :)")