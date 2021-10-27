from ctypes import Array
import problem as prob
from statistics import mean
import time as tt

LL_PARAM = 20
LL_2PARAM = 16
ZM_PARAM = 0.8


def calculateScoreForJob(j, time, problem: prob.SchedulingProblem, last, M):
        zm = max(problem.r[j] - time, problem.s[last][j])
        if(last == -1):
            zm = max(problem.r[j] - time, 0)
        t = zm + time + problem.p[j]
        zm = (zm/M)**2  * ZM_PARAM
        ll = problem.d[j] - t
        if ll > 0:   
            ll = ((ll/M)**2)/(LL_PARAM * problem.n)
        else:
             ll = -((ll/M)**2)/(LL_2PARAM * problem.n)
        return zm + ll

def calculateTimeForJob(j, time, problem: prob.SchedulingProblem, last):
        zm = max(problem.r[j] - time, problem.s[last][j])
        if(last == -1):
            zm = max(problem.r[j] - time, 0)
        t = zm + time + problem.p[j]
        return t

def chooseJob(jobsToUse, time, problem: prob.SchedulingProblem, last, Lmax, M):
    L = max(0, Lmax)
    scores = []  
    for j in jobsToUse:
        scores.append(calculateScoreForJob(j, time, problem, last, M))
    index = 0
    for i in range(len(jobsToUse)):
        if(scores[i] < scores[index]):
            index = i
    return jobsToUse[index]


def solve(problem: prob.SchedulingProblem):
    time_1 = tt.time()
    sol :prob.Solution = prob.Solution(problem.n)
    sol.permutation = []
    jobsToUse = list(range(problem.n))
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
    time_2 = tt.time()
    return sol, time_2-time_1
    
