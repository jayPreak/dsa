class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map = collections.defaultdict(list)
        
        # print(map[3])
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":
                    if c in map:
                        # print("yes")
                        for pos in map[c]:
                            if (pos[0] == i) or (pos[1] == j) or (pos[0]//3 == i//3 and pos[1]//3 == j//3):
                                return False
                    map[c].append((i, j))

        # print(map[3])
        return True
                        