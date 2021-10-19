from ctypes import Array
import problem as prob
from statistics import mean

LL_PARAM = 10

def chooseJob(jobsToUse, time, problem: prob.SchedulingProblem, last, Lmax, M):
    L = max(0, Lmax)
    scores = []  
    for j in jobsToUse:
        zm = max(problem.r[j] - time, problem.s[last][j])
        if(last == -1):
            zm = max(problem.r[j] - time, 0)
        t = zm + time + problem.p[j]
        zm = (zm/M)**2  
        ll = 0
        if(t < problem.d[j]):
            ll = problem.d[j] - t
            ll = ((ll/M)**2)/(LL_PARAM * problem.n)      
        

        scores.append(zm + ll)

    index = 0
    for i in range(len(jobsToUse)):
        if(scores[i] < scores[index]):
            index = i

    return jobsToUse[index]


def solve(problem: prob.SchedulingProblem):
    sol :prob.Solution = prob.Solution(problem.n)
    sol.permutation = []
    jobsToUse = [i for i in range(problem.n)]
    M = max(problem.p)
    time = 0
    last = -1
    Lmax = -100000000
    while(len(jobsToUse) > 0):
        job = chooseJob(jobsToUse, time, problem, last, Lmax, M)
        jobsToUse.remove(job)
        if(last != -1):
            time += problem.s[last][job]
        last = job
        time = max(time, problem.r[job])
        time += problem.p[job]
        L = time - problem.d[job]
        if(L > Lmax):
            Lmax = L
        sol.permutation.append(job)
    sol.Lmax = Lmax
    return sol
    
