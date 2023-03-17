
# global variables
import sys
visited = []
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
total = 70
expanded = 0
count = 0

#class
class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

def create(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)

#moves

def moveLeft(state):
    swap = state.copy()
    index = swap.index(0)
    if index == 0 or index == 3 or index == 6:
        return swap
    else:
        swap[index-1], swap[index] = swap[index], swap[index-1]
        return swap
    
def moveRight(state):
    swap = state.copy()
    index = swap.index(0)
    if index == 2 or index == 5 or index == 8:
        return swap
    else:
        swap[index-1], swap[index] = swap[index], swap[index-1]
        return swap
    
def moveUp(state):
    swap = state.copy()
    index = swap.index(0)
    if index == 0 or index == 1 or index == 2:
        return swap
    else:
        swap[index-1], swap[index] = swap[index], swap[index-1]
        return swap
    
def moveDown(state):
    swap = state.copy()
    index = swap.index(0)
    if index == 6 or index == 7 or index == 8:
        return swap
    else:
        swap[index-1], swap[index] = swap[index], swap[index-1]
        return swap
#expanding node
def expand(node):
    expandedNodes = []

    tempState = moveDown(node.state)
    tempNode = create(tempState, node, "down", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode)

    tempState = moveUp(node.state)
    tempNode = create(tempState, node, "up", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode)

    tempState = moveLeft(node.state)
    tempNode = create(tempState, node, "left", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode)

    tempState = moveRight(node.state)
    tempNode = create(tempState, node, "right", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode)

    return expandedNodes


#bfs XD
