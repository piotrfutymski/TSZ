from array import array
from ctypes import Array
import random

AVERAGE_P = 20
SIGMA_P = 4

AVERAGE_R = -4
SIGMA_R = 4

AVERAGE_D = 0
SIGMA_D = 4

AVERAGE_S = 5
SIGMA_S = 3

SIGMA_SHUFFLE = 4


class SchedulingProblem:
    def __init__(self, n, p, r, d, s):
        self.n = n
        self.p = p
        self.r = r
        self.d = d
        self.s = s

    def __init__(self):
        self.n = 0

    def __init__(self, n):
        self.n = n
        self.p = [0] * n
        self.r = [0] * n
        self.d = [0] * n
        self.s = [[0] * n for i in range(n)]
        
    def saveToFile(self, filename):
        f = open(filename, "w")
        f.write(str(self.n))
        f.write("\n")
        for i in range(self.n):        
            f.write(str(self.p[i]) + " " + str(self.r[i]) + " " + str(self.d[i]))
            f.write("\n")
        for i in range(self.n):        
            f.write(" ".join([str(k) for k in self.s[i]]))
            f.write("\n") 

    def loadFromFile(self, filename):
        f = open(filename, "r")
        line = f.readline().split(" ")
        n = int(line[0])
        self.n = n
        self.p = [0] * n
        self.r = [0] * n
        self.d = [0] * n
        self.s = [[0] * n for i in range(n)]
        for i in range(self.n): 
            line = f.readline().split(" ")
            self.p[i] = int(line[0])
            self.r[i] = int(line[1])
            self.d[i] = int(line[2])
        for i in range(self.n):
            line = f.readline().split(" ")
            for j in range(self.n):
                self.s[i][j] = int(line[j])


class Solution:
    def __init__(self, n, permutation, Lmax):
        self.n = n
        self.permutation = permutation
        self.Lmax = Lmax
    
    def __init__(self, n):
        self.n = n
        self.permutation = [i for i in range(0, n)]
        self.Lmax = 0

    def loadFromFile(self, filename):
        f = open(filename, "r")
        line = f.readline().split(" ")
        self.permutation = [0] * self.n
        self.Lmax = 0
        self.Lmax = int(line[0])
        line = f.readline().split(" ")
        for i in range(self.n): 
            self.permutation[i] = int(line[i])

    def saveToFile(self, filename):
        f = open(filename, "w")
        f.write(str(self.Lmax))
        f.write("\n")
        f.write(" ".join([str(k) for k in self.permutation]))       



def generate(n):
    problem = SchedulingProblem(n)  

    for i in range(n):
        for j in range(i):
            s = int(random.gauss(AVERAGE_S, SIGMA_S))
            if(s < 0):
                s = 0
            if(j == i - 1):
                s += int(SIGMA_S * 1.5)
            problem.s[i][j] = s
            problem.s[j][i] = s           
        problem.s[i][i] = 0

    time = 0
    time_good = 0

    for i in range(n):
        p = int(random.gauss(AVERAGE_P, SIGMA_P))
        if(p < 1):
            p = 1
        problem.p[i] = p

        r = int(random.gauss(AVERAGE_R, SIGMA_R))
        r = r + time_good
        if(r < 0 ):
            r = 0
        problem.r[i] = r

        if(r > time):
            time = r
        time += p
        time_good += p

        d = int(random.gauss(AVERAGE_D, SIGMA_D))
        d = d + time
        if(d < r + p):
            d = r + p
        problem.d[i] = d     

        if(i+1 < n):
            time += problem.s[i][i+1]
            time_good += int(problem.s[i][i+1] - SIGMA_S * 1.5)

    for l in range(int(n*2.0/3.0)):
        i = 0
        j = 0
        while (i == j):
            i = random.randint(0,n-1)
            j = random.randint(0,n-1)
        
        r = min(problem.r[i], problem.r[j])
        problem.r[i] = max(0, int(random.gauss(0,SIGMA_SHUFFLE)) + r)
        problem.r[j] = max(0, int(random.gauss(0,SIGMA_SHUFFLE)) + r)

        d = max(problem.d[i], problem.d[j])
        problem.d[i] = max(problem.r[i] + problem.p[i], int(random.gauss(-5,SIGMA_SHUFFLE)) + d)
        problem.d[j] = max(problem.r[j] + problem.p[j], int(random.gauss(-5,SIGMA_SHUFFLE)) + d)

    problem.r[problem.r.index(min(problem.r))] = 0

    return problem

