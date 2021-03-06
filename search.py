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


#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
num_hours_i_spent_on_this_assignment = 13
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

"""
#####################################################
#####################################################



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






def depthFirstSearch(problem):
    """
    Questoin 1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )

    """
    "*** YOUR CODE HERE ***"


    
    frontier = util.Stack() #main stack of work

    frontier.push(problem.getStartState()) #push starting state onto stack
    currpath = util.Stack() #list of nodes visited from start to current
    visited = set() # list that keeps track of which states have been visited
    finalpath = []    #Resulting list of nodes (blocks) visited
    current = frontier.pop() #current state


   ## print ( problem.getStartState() )

    while problem.isGoalState(current) == False:
        
        if current in visited:
            pass


        else:
            visited.add(current)
            successors = problem.getSuccessors(current)

            for child,direction,cost in successors:
                temp = finalpath + [direction]
                currpath.push(temp)
                frontier.push(child)
      

        current = frontier.pop()
        finalpath = currpath.pop()

        
    return finalpath



def breadthFirstSearch(problem):
    """Questoin 1.2
     Search the shallowest nodes in the search tree first.
     """
    "*** YOUR CODE HERE ***"
    
    
    frontier = util.Queue() #main queue of work
    frontier.push(problem.getStartState()) #push starting state onto queue
    currpath = util.Queue()#list of nodes visited from start to current
    visited = [] # list that keeps track of which states have been visited
    finalpath = [] #Resulting list of nodes (blocks) visited
    current = frontier.pop() #current state
    temp = []

    while problem.isGoalState(current) == False:

        if current in visited:
            pass

        else:
            visited.append(current) 
            successors = problem.getSuccessors(current) 

            for child,direction,cost in successors:
                frontier.push(child)
                temp = finalpath + [direction]
                currpath.push(temp)
           

        #print (current)
        current = frontier.pop()
        finalpath = currpath.pop()
        
    return finalpath

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Question 1.3
    Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))
    visited = []

    while frontier:
        last, current = frontier.pop()

        if problem.isGoalState(last) == True:
            return current

        if last not in visited:
            visited.append(last)

        for successor in problem.getSuccessors(last):
            if(successor[0] in visited):
                continue;
            frontier.push((successor[0], current + [successor[1]]), problem.getCostOfActions(current + [successor[1]]) + heuristic(successor[0], problem))

    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
