
# global variables
# import sys
visited = []
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
total = 70
expanded = 0
count = 0

# class


class Node:
    def __init__(self, state, parent, child, depth, cost):
        self.state = state
        self.parent = parent
        self.child = child
        self.depth = depth
        self.cost = cost

# def create(state, parent, child, depth, cost):
#     return Node(state, parent, child, depth, cost)

# moves


def moveLeft(state):
    swap = state.copy()
    indxx = swap.index(0)
    if (indxx == 0 or indxx == 3 or indxx == 6):
        return swap
    else:
        swap[indxx-1], swap[indxx] = swap[indxx], swap[indxx-1]
        return swap


def moveRight(state):
    swap = state.copy()
    indxx = swap.index(0)
    if (indxx == 2 or indxx == 5 or indxx == 8):
        return swap
    else:
        swap[indxx-1], swap[indxx] = swap[indxx], swap[indxx-1]
        return swap


def moveUp(state):
    swap = state.copy()
    indxx = swap.index(0)
    if (indxx == 0 or indxx == 1 or indxx == 2):
        return swap
    else:
        swap[indxx-3], swap[indxx] = swap[indxx], swap[indxx-3]
        return swap


def moveDown(state):
    swap = state.copy()
    indxx = swap.index(0)
    if (indxx == 6 or indxx == 7 or indxx == 8):
        return swap
    else:
        swap[indxx-3], swap[indxx] = swap[indxx], swap[indxx-3]
        return swap
# expanding node


def expand(node):
    # print("hi")
    expandedNodes = []

    tempState1 = moveDown(node.state)
    tempNode1 = Node(tempState1, node, "down", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode1)

    tempState2 = moveUp(node.state)
    tempNode2 = Node(tempState2, node, "up", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode2)

    tempState3 = moveLeft(node.state)
    tempNode3 = Node(tempState3, node, "left", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode3)

    tempState4 = moveRight(node.state)
    tempNode4 = Node(tempState4, node, "right", node.depth+1, node.cost+1)
    expandedNodes.append(tempNode4)

    return expandedNodes


# bfs XD
def bfs(start, goal):
    if (start == goal):
        return [None]
    else:
        toBeExpanded = []
        currNode = Node(start, None, None, 0, 0)
        toBeExpanded.append(currNode)

        for i in range(total):
            tempExpanded = []
            size = len(toBeExpanded)
            for j in range(size):
                if (toBeExpanded[j] in visited):
                    continue

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

# yep


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

            while (flag):
                parent = curr.parent
                prevState = parent.state
                path.append(prevState)
                curr = parent

                if (prevState == startingState):
                    flag = False

            path.reverse()
            print()
            print("Stepwise Sequence of states: ")
            for state in path:
                print(state[0], " | ", state[1], " | ", state[2])
                print(state[3], " | ", state[4], " | ", state[5])
                print(state[6], " | ", state[7], " | ", state[8])
                print()
    else:
        print("invalid input tbh")


if __name__ == "__main__":
    board = "1,2,5,3,4,0,6,7,8"
    main(board)
