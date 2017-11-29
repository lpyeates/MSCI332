import copy as copy
import random
import numpy as np
class solutionSet:
    #This is the class to hold the solution sets
    def __init__(self):
        self.routesUsed = [[],[]]
        self.flightsCovered = []
    def addcoverage(self, addingRoutes):
        length = len(addingRoutes)
        checkLength = len(self.flightsCovered)
        i = 0
        if checkLength == 0:
            while i < length:
                #print(addingRoutes[i])
                self.flightsCovered.append(addingRoutes[i])
                i += 1
        else:
            i = 1
            while i < length - 1:
                #print(addingRoutes[i])
                self.flightsCovered.append(addingRoutes[i])
                i += 1
    def removeroute(self,toRemove):
        newFlightsCovered = []
        lengthOfCovered = len(self.flightsCovered)
        i = 0
        while i < lengthOfCovered:
            checkOverlap = False
            j = 1
            lengthToRemove = len(toRemove) - 1
            while j < lengthToRemove:
                if self.flightsCovered[i]==toRemove[j]:
                    checkOverlap = True
                j += 1
            if checkOverlap == False:
                newFlightsCovered.append(self.flightsCovered[i])
            i += 1
        #print(newFlightsCovered)
        self.flightsCovered = newFlightsCovered
        newRoutesUsed = [[],[]]
        lengthofRoutes = len(self.routesUsed)
        k = 0
        while k < lengthofRoutes - 1:
            if self.routesUsed[k] != toRemove:
                if newRoutesUsed[0] == []:
                    newRoutesUsed[0] = self.routesUsed[k]
                elif newRoutesUsed[1] == []:
                    newRoutesUsed[1] = self.routesUsed[k]
                else:
                    newRoutesUsed.append([])
                    newRoutesUsed[len(newRoutesUsed) - 1] = self.routesUsed[k]
            k += 1
        self.routesUsed = newRoutesUsed
    def getrouteslength(self):
        length = 0
        i = 0
        holdRoutes = self.routesUsed
        #print(len(holdRoutes))
        while i < len(self.routesUsed):
            length += 1
            i += 1
        return length
    def clearsolutionset(self):
        self.routesUsed = []
        self.flightsCovered = []
        return self
    def addroute(self, addingRoute):
        if self.routesUsed[0] == []:
            self.routesUsed[0] = addingRoute
        elif self.routesUsed[1] == []:
            self.routesUsed[1] = addingRoute
        else:
            self.routesUsed.append([])
            self.routesUsed[len(self.routesUsed)-1] = addingRoute
