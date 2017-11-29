#Basis for the simulated annealing was taught to me by Hannah Gautreau
#Some logic was used in her CS 686(Artifical Intelligence) course Assignment 2
#here is a link to the github repo: https://github.com/gauhannah/CS686A2-TSP
#The code here is different as it solves another problem but some logic comes from there
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import queue as queue
import copy as copy
import random
import math
from solutionSet import solutionSet
from OptimalSolutions import optimalSolutions

def checkForOverlap(currentSolution, addingRoute):
    """This function checks to see if the new route can be added"""
    i=0
    lengthCurrent = len(currentSolution)
    while i < lengthCurrent:
        j = 1
        lengthAdding = len(addingRoute)-1
        #print(addingRoute)
        while j < lengthAdding:
            checkingFlight = addingRoute[j]
            if currentSolution[i] == checkingFlight:
                return True
            j += 1
        i += 1
    return False


def addRoutes(currentSolution, allPaths):
    """This function adds routes that do not overlap with the current solution"""
    #print(len(allPaths))
    #print(allPaths)
    i = 0
    length = len(allPaths)
    while i < length:
        addingRoute = allPaths[i]
        testOverlpp = checkForOverlap(currentSolution.flightsCovered, addingRoute)
        if testOverlpp == False:
            currentSolution.addroute(addingRoute)
            currentSolution.addcoverage(addingRoute)
        i+= 1
    return currentSolution

def cleanAddingPaths(allPaths, leavingPath):
    cleanPaths = []
    i = 0
    length = len(allPaths)
    while i < length:
        reAdd = np.array_equal(leavingPath, allPaths[i])
        if reAdd == False:
            cleanPaths.append(allPaths[i])
        i += 1
    return cleanPaths





# code found from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# Uses logic from MSCI 240 modified for python instead of java
#initialize empty opject
object = []
i = 0
lengthOfPaths = 0
#The following code takes the adj. matrix and outputs all possible routes
#The first part reads in the .txt file
#The .txt file is edited to remove the rows with strings
#Read in adj. matrix
#adjMatrix = pd.read.txt('sampleData.txt')
with open('adjecency_matrix.txt') as adjMatrix:
    for line in adjMatrix:
        temp = line.split()
        object.append([])
        for j in range(173):
            if int(temp[j]) == 1:
                object[i].append(j)
        i += 1

#Breadth first search to get all possible routes
print('done reading')
paths = []
path = []
q = queue.Queue()
q.put([0])
while not q.empty():

    path = q.get()
    for a in (range(1,173)):
        tmp = copy.copy(path)
        if a in object[tmp[len(tmp)-1]]:
            tmp.append(a)
            if tmp[len(tmp)-1] == 173:
                #print("in if")
                #print(tmp)
                paths.append(tmp)
                lengthOfPaths = lengthOfPaths + 1
                #path = q.get()
            elif len(tmp) > 10:
                print('route too long')
            elif q.qsize() < 1000000:

                q.put(tmp)




#prints all paths

with open('results.txt', 'w') as results:
    results.write(paths)
    results.write('done paths')

    print(lengthOfPaths)
    rand = random.randint(0,lengthOfPaths - 1)
    #print(rand)
    routes = []
    flightsCovered = []
    temp = 65
    k = 0.5
    alpha = 0.9
    stopPoint = 5

    #handles adding the initial route randomly
    bestSolution = optimalSolutions()
    a = 0
    totalSolutions = 10
    while a < totalSolutions:
        optimalSolution = solutionSet()
        rand = random.randint(0, lengthOfPaths - 1)
        routeToAdd = paths[rand]
        optimalSolution.addroute(routeToAdd)
        optimalSolution.addcoverage(routeToAdd)
        solution = solutionSet()
        solution.addroute(routeToAdd)
        solution.addcoverage(routeToAdd)

        addRoutes(solution, paths)
        results.write('starting coverage:')
        results.write(optimalSolution.flightsCovered)
        loops = 10
        i = 0
        while i < loops:
            temp = 65
            while temp > stopPoint:
                #print('loop')
                challengSet = solutionSet()
                k = 0
                lengthOfCurrentSol = len(solution.routesUsed)
                while k < lengthOfCurrentSol:
                    challengSet.addroute(solution.routesUsed[k])
                    k += 1
                challengSet.addcoverage(solution.flightsCovered)
                currentSolutionLength = challengSet.getrouteslength()
                rand = random.randint(0,currentSolutionLength-1)
                leaving = challengSet.routesUsed[rand]
                cleanedPaths = cleanAddingPaths(paths, leaving)
                challengSet.removeroute(leaving)
                addRoutes(challengSet, cleanedPaths)
                solutionlength = len(solution.flightsCovered)
                challengelength = len(challengSet.flightsCovered)
                moveNeighborhood = random.uniform(0,1)
                if(challengelength>solutionlength):
                    solution.clearsolutionset()
                    solution = copy.deepcopy(challengSet)
                elif(moveNeighborhood >= 0.95):
                    solution.clearsolutionset()
                    solution = copy.deepcopy(challengSet)

                temp = temp /(1 + alpha * math.log1p(k))
            #print('The Solution the this pass is:')
            #print(solution.flightsCovered)
            currentOptimalCoverage = len(optimalSolution.flightsCovered)
            challengeCoverage = len(solution.flightsCovered)

            if(challengeCoverage >= currentOptimalCoverage):
                optimalSolution.clearsolutionset()
                optimalSolution = copy.deepcopy(solution)

            i += 1

        #print('the final solution is:')
        #print(optimalSolution.flightsCovered)
        bestSolution.addSolution(optimalSolution)
        a += 1
    results.write(' the most optimal solution is:')
    results.write(bestSolution.optimalSolution)
    results.write(bestSolution.optimalRoute)
    results.close()





#print(object)
#below is the training code. It's how I relearn depth and bredth first search
#It has been commented out and no longer affect the program
''''#get routes
graph = {'0': set(['1', '2']),
         '1': set(['4']),
         '2': set(['D']),
         '3': set(['4', 'D']),
         '4': set(['5', 'D']),
         '5': set(['D', ]),
         'D': set([])}

def dfs_paths(object, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in object[vertex] - set[path]:
            if next == goal:
                # print(path + [next] + '\n')
                yield path + [next]
            else:
                stack.append((next, path + [next]))
print(list(dfs_paths(object, 0, 7)))'''


