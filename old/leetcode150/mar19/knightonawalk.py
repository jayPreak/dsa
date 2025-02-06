# class Node:
#     def __init__(self, state, parent, operator, depth, cost):
#         self.state = state
#         self.parent = parent
#         self.operator = operator
#         self.depth = depth
#         self.cost = cost

# def create(state, parent, operator, depth, cost):
#     return Node(state, parent, operator, depth, cost)

# #moves



#XDD


# class Solution:
#     def checkValidGrid(self, grid: List[List[int]]) -> bool:
#         n = len(grid)
#         visited = [False] * (n * n)
#         directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        
#         def dfs(row, col, move):
#             if move == n * n:
#                 return True
#             index = grid[row][col]
#             if visited[index]:
#                 return False
#             visited[index] = True
#             for dx, dy in directions:
#                 new_row, new_col = row + dx, col + dy
#                 if 0 <= new_row < n and 0 <= new_col < n and dfs(new_row, new_col, move + 1):
#                     return True
#             visited[index] = False
#             return False
        
#         # Find the starting position of the knight
#         start = None
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     start = (i, j)
#                     break
#             if start:
#                 break
#         return dfs(start[0], start[1], 1)
        

class Solution:
    def validPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        visited = set()
        dx = [-2, -2, -1, -1, 1, 1, 2, 2]
        dy = [-1, 1, -2, 2, -2, 2, -1, 1]

        def dfs(row, col, count):
            if count == n * n:
                return True
            visited.add((row, col))
            for i in range(8):
                r, c = row + dx[i], col + dy[i]
                if 0 <= r < n and 0 <= c < n and (r, c) not in visited and grid[r][c] == count:
                    if dfs(r, c, count + 1):
                        return True
            visited.remove((row, col))
            return False

        return dfs(0, 0, 1)

#chatgpt my king