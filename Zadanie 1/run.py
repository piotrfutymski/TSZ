from statistics import mean, median
import utils, algorithm
import problem as prob
from os import walk, path

filenames = next(walk("in/"), (None, None, []))[2]  # [] if no file

values = []

def generateSoultions():
    for file in filenames:
        problem = prob.SchedulingProblem(0)
        problem.loadFromFile("in/"+ file)
        a = algorithm.solve(problem)
        values.append(a.Lmax)
        a.saveToFile("out/"+ file)

def weryfikacjaAll():
    for file in filenames:
        utils.weryfikacja(file)


generateSoultions()
weryfikacjaAll()
print("Mean:\t" + str(mean(values)))
print("Median:\t" + str(median(values)))