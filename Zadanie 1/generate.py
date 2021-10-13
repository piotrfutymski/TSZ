import problem

for n in range(5,55,5):
    prob = problem.generate(n)
    prob.saveToFile("in/141216_" + str(n) + ".txt")