# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def retrace_path(parents, beginning, end, problem):
    """ Once we've found the reward, we need to regenerate the steps we took to
    attain it. We can do this by traversing the graph from end to beginning, using
    the dictionary of parents we compiled to do so.
    """

    steps = []

    s = beginning

    while s != end:

        # Specify the state we're trying to get to, which is the parent of the current one
        target = parents[s]

        # Add the step to reach the child from the parent
        steps.extend([d[1] for d in problem.getSuccessors(target) if d[0] == s])

        # Update the current step
        s = target

    # We now have an (inverted) list of directions from end -> beginning; reverse to get beginning -> end
    steps.reverse()

    return steps


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    S = util.Stack()

    visited = util.Stack()  # Will store the visited states
    parents = {}  # Will store the parent states of visited states

    c = problem.getStartState()
    S.push(c)  # Put our first state in the stack

    #  Whilst we still have unvisited states
    while S.isEmpty() is False:

        # Mark the current state as visited
        visited.push(c)

        # If this is actually a goal state, we need to reconstruct the path and return it
        if problem.isGoalState(c):
            return retrace_path(parents, c, problem.getStartState(), problem)

        # Put all of the adjacent states in the stack, if they're neww
        for successor in problem.getSuccessors(c):
            if successor[0] not in visited.list:
                S.push(successor[0])
                parents[successor[0]] = c

        # And generate a new unexplored state
        c = S.pop()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.

    The sole difference with depth-first search is in the choice
    of data structure; here we use a queue, which is FIFO (First One
    In, First One Out)"""

    S = util.Queue()

    visited = util.Queue()  # Will store the visited states
    parents = {}  # Will store the parent states of visited states

    c = problem.getStartState()
    S.push(c)  # Put our first state in the stack

    #  Whilst we still have unvisited states
    while S.isEmpty() is False:

        # Mark the current state as visited
        visited.push(c)

        # If this is actually a goal state, we need to reconstruct the path and return it
        if problem.isGoalState(c):
            return retrace_path(parents, c, problem.getStartState(), problem)

        # Put all of the adjacent states in the stack, if they're neww
        for successor in problem.getSuccessors(c):
            if successor[0] not in visited.list:
                S.push(successor[0])
                parents[successor[0]] = c

        # And generate a new unexplored state
        c = S.pop()



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
