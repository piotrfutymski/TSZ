import time as tt
import sys

class SchedulingProblem:
    def __init__(self, n, p, r, d, w, b):
        self.n = n
        self.p = p
        self.r = r
        self.d = d
        self.w = w
        self.b = b

    def __init__(self):
        self.n = 0

    def __init__(self, n):
        self.n = n
        self.p = [0] * n
        self.r = [0] * n
        self.d = [0] * n
        self.w = [0] * n
        self.b = [0] * 4
        
    def saveToFile(self, filename):
        f = open(filename, "w")
        f.write(str(self.n))
        f.write("\n")
        for i in range(len(self.b) - 1):
            f.write(str(self.b[i]))
            f.write(" ")
        f.write(str(self.b[3]))
        f.write("\n")
        for i in range(self.n):        
            f.write(str(self.p[i]) + " " + str(self.r[i]) + " " + str(self.d[i]) + " " + str(self.w[i]))
            f.write("\n")

    def loadFromFile(self, filename):
        f = open(filename, "r")
        line = f.readline().split(" ")
        n = int(line[0])
        self.n = n
        self.p = [0] * n
        self.r = [0] * n
        self.d = [0] * n
        self.w = [0] * n
        self.b = [0] * 4
        line = f.readline().split(" ")
        for i in range(len(line)):
            self.b[i] = float(line[i])
        for i in range(self.n): 
            line = f.readline().split(" ")
            self.p[i] = float(line[0])
            self.r[i] = float(line[1])
            self.d[i] = float(line[2])
            self.w[i] = float(line[3])


class Solution:
    def __init__(self, n, permutation, res):
        self.n = n
        self.permutation = permutation
        self.res = res
    
    def __init__(self, n:int):
        self.n = n
        self.permutation = []
        i = 1
        for j in range(3):
            self.permutation.append([k for k in range(i, i+int(n/4))])
            i = i+int(n/4)
        self.permutation.append([k for k in range(i, n+1)])
        self.res = 0

    def loadFromFile(self, filename):
        f = open(filename, "r")
        line = f.readline().split(" ")
        self.res = float(line[0])
        self.permutation = []
        n = 0
        for i in range(4):
            self.permutation.append([])
            allLine = f.readline()
            if(allLine != '\n'):
                line = allLine.split(" ")
                for j in range(len(line)): 
                    self.permutation[i].append(int(line[j]))
                    n += 1
        self.n = n

    def saveToFile(self, filename):
        f = open(filename, "w")
        f.write(str(self.res))
        f.write("\n")
        for i in range(4):
            f.write(" ".join([str(k) for k in self.permutation[i]]))
            f.write("\n")  


PARAM = 16

def existsMachineWithLowerT(j, times, problem: SchedulingProblem):
    for i in range(len(times)):
        if(problem.r[j] > times[i]):
            return True
    return False

def calculateScoreForJob(j, times, problem: SchedulingProblem, M, W):
        zm_tab = []
        numOFLate = 0
        avaibleMachine = []
        for i in range(len(times)):
            zm = problem.r[j] - times[i]
            if(zm < 0):
                zm = 0
            t = zm + times[i] + problem.p[j] / problem.b[i]
            zm = ((zm/M)**2)* problem.b[i]       
            ll = problem.d[j] - t
            if(ll < 0):
                numOFLate+=1
            else:
                ll = (ll/(PARAM*M))**2
                avaibleMachine.append(i) 
            zm_tab.append(zm+ll)  

        if(numOFLate == len(times)):
            return sys.float_info.max, 0
        if(numOFLate <= 2):
            numOFLate = 0
        else:
            numOFLate = problem.w[j]/(100*W)

        num = avaibleMachine[0]
        value = zm_tab[num]
        for machine in avaibleMachine:
            if zm_tab[machine] < value:
                value = zm_tab[machine]
                num = machine
        res = value - numOFLate**2 

        return res, num

def chooseJob(jobsToUse, times, problem: SchedulingProblem, M, W):
    scores = []  
    for j in jobsToUse:
        scores.append(calculateScoreForJob(j, times, problem, M, W))
    index = 0
    machine = scores[0][1]
    for i in range(len(jobsToUse)):
        if(scores[i][0] < scores[index][0]):
            index = i
            machine = scores[i][1]
    return jobsToUse[index], machine

def solve(problem: SchedulingProblem):
    sol = Solution(problem.n)
    sol.permutation = []
    for i in range(4):
        sol.permutation.append([])
    jobsToUse = list(range(problem.n))
    M = max(problem.p)
    W = max(problem.w)
    times = [0.0, 0.0, 0.0, 0.0]
    res = 0
    while(len(jobsToUse) > 0):
        job = chooseJob(jobsToUse, times, problem, M, W)
        jobsToUse.remove(job[0])
        times[job[1]] = max(times[job[1]], problem.r[job[0]])
        times[job[1]] += problem.p[job[0]]/problem.b[job[1]]
        L = times[job[1]] - problem.d[job[0]]
        if(L > 0):
            res += problem.w[job[0]]
        sol.permutation[job[1]].append(job[0]+1)
    sol.res = res
    return sol

time = 0

def generateSoultions(file):
    problem = SchedulingProblem(0)
    problem.loadFromFile("in/"+ file)
    time_1 = tt.time() * 1000
    a = solve(problem)
    time_2 = tt.time() * 1000
    a.saveToFile("out/"+ file)
    print(str(a.res)+"\t->\t" + file + "\t" + str(time_2-time_1) + " - time in [ms]")
        

indexes = ["141216", "141220", "141244", "141286", "141317", "141320", "141337"]


#for index in indexes:
#    for i in range(50,550,50):
#        generateSoultions(index + "_" + str(i)+".txt")


generateSoultions(sys.argv[1])