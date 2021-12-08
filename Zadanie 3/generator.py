import random
from objects import SchedulingProblem

AVERAGE_P = [[20,20,20,5],[45,10,15,2],[5,10,30,10], [10,40,15,3]]
SIGMA_P = 0.2

D_0 = 70
D = 25
SIGMA_D = 0.5
A = [7,1,4,2]
B = [3,9,6,8]

def generate(n):
    problem = SchedulingProblem(n)
    time = D_0
    for i in range(n):
        index = random.randint(0,3)
        for j in range(4):
            problem.p[i][j] = max(1, int(random.gauss(AVERAGE_P[index][j], int(AVERAGE_P[index][j] * SIGMA_P))))
        problem.d[i] = max(0, time + int(random.gauss(0, int(D * SIGMA_D))))
        time += D 
        problem.a[i] = A[index]
        problem.b[i] = B[index]
        if(i == int((n*4)/5)):
            time = D_0
    return problem


for n in range(50,550,50):
    prob = generate(n)
    prob.saveToFile("in/141216_" + str(n) + ".txt")