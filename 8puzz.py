
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

    tempState1 = moveDown(node.state)
    tempNode1 = create(tempState1, node, "down", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode1)

    tempState2 = moveUp(node.state)
    tempNode2 = create(tempState2, node, "up", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode2)

    tempState3 = moveLeft(node.state)
    tempNode3 = create(tempState3, node, "left", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode3)

    tempState4 = moveRight(node.state)
    tempNode4 = create(tempState4, node, "right", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode4)

    return expandedNodes


#bfs XD
def bfs(start, goal):
    if (start==goal):
        return [None]
    else:
        toBeExpanded = []
        currNode = create(start, None, None, 0, 0)
        toBeExpanded.append(currNode)

        for i in range(total):
            tempExpanded = []
            size = len(toBeExpanded)
            for j in range(size):
                if(toBeExpanded[j] in visited):
                    continue;

                nodeList = expand(toBeExpanded[j])

                for x in range(4):
                    if (nodeList[x].state == goal):
                        count = i+1
                        print()
                        print("Goal State found.", nodeList[x].state)
                        print()
                        print("0 | 1 | 2")
                        print("3 | 4 | 5")
                        print("6 | 7 | 8")
                        return nodeList[x]
                    else:
                        tempExpanded.append(nodeList[x])
                        visited.append(nodeList[x].state)
            
            toBeExpanded.clear()
            toBeExpanded = tempExpanded.copy()
            tempExpanded.clear()
    return None

#yep

def main(board):
    method = 'bfs'
    leng = 0
    x = 1
    boardSplit = board.split(",")
    startingState = [int(i) for i in boardSplit]
    print("Starting State: ")
    print(startingState)


    if (len(startingState) == 9):
        res = bfs(startingState, goal)
        if res == None:
            print("No solution found. ")
        elif res == [None]:
            print("Start Node was the goal. lol")
        else:
            print()
            print("Total moves used: ", res.cost)
            path = []
            path.append(res.state)
            curr = res

            flag = True

            while(flag):
                parent = curr.parent
                prevState = parent.state
                path.append(prevState)
                curr = parent

                if(prevState == startingState):
                    flag = False
            
            path.reverse()
            print()
            print("Stepwise Sequence of states: ")
            for state in path:
                print(state[0] , " | " , state[1], " | ", state[2])
                print(state[3] , " | " , state[4], " | ", state[5])
                print(state[6] , " | " , state[7], " | ", state[8])
                print()
    else:
        print("invalid input tbh")

if __name__ == "__main__":
    board = "1,2,5,3,4,0,6,7,8"
    main(board)
