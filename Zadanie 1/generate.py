import problem

for n in range(50,550,50):
    prob = problem.generate(n)
    prob.saveToFile("in/141216_" + str(n) + ".txt")