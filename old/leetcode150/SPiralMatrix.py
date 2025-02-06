class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # (list(zip(*matrix)))[::-1]

        res = []
        while matrix:
            res += matrix.pop(0)
            # print((list(zip(*matrix)))[::-1])
            matrix = (list(zip(*matrix)))[::-1]
            # print(matrix)

        return res