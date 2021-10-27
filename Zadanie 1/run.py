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
        values.append(a[1])
        a[0].saveToFile("out/"+ file)

def weryfikacjaAll():
    i = 0
    for file in filenames:
        utils.weryfikacja(file, values[i])
        i+=1


generateSoultions()
weryfikacjaAll()