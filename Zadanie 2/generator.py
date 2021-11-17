import random
from objects import SchedulingProblem

AVERAGE_P = 20
SIGMA_P = 8

MIN_D = 0
MAX_D = 180

W_DIV = 60

def generate(n):
    problem = SchedulingProblem(n)
    problem.b[0] = 1
    problem.b[1] = int(random.randint(2,5))
    problem.b[2] = int(random.randint(1,3))
    problem.b[3] = 10 - problem.b[1] - problem.b[2] - problem.b[3]

    i = 0
    time = 0
    while(i < n):
        if(random.randint(0,1) == 1):
            p = int(random.gauss(AVERAGE_P, SIGMA_P))
            if(p < 1):
                p = 1
            problem.p[i] = p
            problem.r[i] = time
            d = random.randint(MIN_D, MAX_D)
            problem.d[i] = time + p + d
            problem.w[i] = int(1 + (random.randint(MIN_D, MAX_D) + d) / W_DIV)
            i += 1 
        time += 1
    return problem


for n in range(5,10,50):
    prob = generate(n)
    prob.saveToFile("in/141216_" + str(n) + ".txt")