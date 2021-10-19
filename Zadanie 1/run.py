import utils, algorithm
import problem as prob
from os import walk, path

filenames = next(walk("in/"), (None, None, []))[2]  # [] if no file

def generateSoultions():
    for file in filenames:
        problem = prob.SchedulingProblem(0)
        problem.loadFromFile("in/"+ file)
        algorithm.solve(problem).saveToFile("out/"+ file)

def weryfikacjaAll():
    for file in filenames:
        utils.weryfikacja(file)



generateSoultions()
weryfikacjaAll()