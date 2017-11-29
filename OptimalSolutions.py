import copy as copy
class optimalSolutions:
    def __init__(self):
        self.solutions = [[],[]]
        self.optimalSolution = []
        self.optimalRoute = []
    def addSolution(self, addingRoute):
        if self.solutions[0] == []:
            self.solutions[0] = addingRoute.flightsCovered
        elif self.solutions[1] == []:
            self.solutions[1] = addingRoute.flightsCovered
        else:
            self.solutions.append([])
            self.solutions[len(self.solutions)-1] = addingRoute.flightsCovered
        if len(addingRoute.flightsCovered) > len(self.optimalSolution):
            self.optimalRoute = copy.deepcopy(addingRoute.routesUsed)
            self.optimalSolution = addingRoute.flightsCovered

