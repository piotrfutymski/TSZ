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
    
    def __init__(self, n):
        self.n = n
        self.permutation = []
        i = 1
        for j in range(3):
            self.permutation.append([k for k in range(i, i+n/4)])
            i = i+n/4
        self.permutation.append([k for k in range(i, n+1)])
        self.res = 0

    def loadFromFile(self, filename):
        f = open(filename, "r")
        line = f.readline().split(" ")
        self.res = int(line[0])
        self.permutation = []
        n = 0
        for i in range(4):
            line = f.readline().split(" ")
            self.permutation.append([])
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