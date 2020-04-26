from chapt3.cs188_search import util


class SearchProblem:
        def getStartState(self):
            util.raiseNotDefined()

        def isGoalState(self, state):
            util.raiseNotDefined()

        def getSuccessor(selfs, state):
            util.raiseNotDefined()

        def getCostOfAction(self, actions):
            util.raiseNotDefined()

def depthFirstSearch(problem):

    def Recursive_DFS(node, problem, solution, closeSet):
        if problem.isGoalState(node):
            return solution

        else:
            for child, direction, cost in problem.getSuccessor(node):
                if child not in closeSet:
                    solution.append(direction)
                    closeSet.add(child)
                    result = Recursive_DFS(child, problem, solution, closeSet)

                    if result:
                        return solution

                    else:
                        solution.pop()
                else:
                    return False

            solution = []
            closeSet = set()
            closeSet.add(problem.getStartState())
            solution = Recursive_DFS(problem.getStartState(), problem, closeSet)
            return solution

