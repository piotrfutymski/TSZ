class SchedulingProblem:
    def __init__(self, n, p, d, a, b):
        self.n = n
        self.p = p
        self.d = d
        self.a = a
        self.b = b

    def __init__(self):
        self.n = 0

    def __init__(self, n):
        self.n = n
        self.p = []
        for i in range(n):
            self.p.append([0]*n)
        self.d = [0] * n
        self.a = [0] * n
        self.b = [0] * n
        
    def saveToFile(self, filename):
        f = open(filename, "w")
        f.write(str(self.n))
        f.write("\n")
        for i in range(self.n):       
            f.write(str(self.p[i][0]) + " " + str(self.p[i][1]) + " " + str(self.p[i][2]) + " " + str(self.p[i][3]) +
            " " + str(self.d[i]) + " " + str(self.a[i]) + " " + str(self.b[i]))
            f.write("\n")

    def loadFromFile(self, filename):
        f = open(filename, "r")
        line = f.readline().split(" ")
        n = int(line[0])
        self.n = n
        self.p = []
        for i in range(n):
            self.p.append([0]*n)
        self.d = [0] * n
        self.a = [0] * n
        self.b = [0] * n
        line = f.readline().split(" ")
        for i in range(self.n): 
            line = f.readline().split(" ")
            self.p[i][0] = float(line[0])
            self.p[i][1] = float(line[1])
            self.p[i][2] = float(line[2])
            self.p[i][3] = float(line[3])
            self.d[i] = float(line[4])
            self.a[i] = float(line[5])
            self.b[i] = float(line[6])


class Solution:
    def __init__(self, n, permutation, res):
        self.n = n
        self.permutation = permutation
        self.res = res
    
    def __init__(self, n:int):
        self.n = n
        self.permutation = [k for k in range(1, n+1)]
        self.res = 0

    def loadFromFile(self, filename):
        f = open(filename, "r")
        line = f.readline().split(" ")
        self.res = float(line[0])
        self.permutation = []
        n = 0
        allLine = f.readline()
        if(allLine != '\n'):
            line = allLine.split(" ")
            for j in range(len(line)): 
                self.permutation.append(int(line[j]))
                n += 1  
        self.n = n

    def saveToFile(self, filename):
        f = open(filename, "w")
        f.write(str(self.res))
        f.write("\n")
        f.write(" ".join([str(k) for k in self.permutation]))  