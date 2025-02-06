class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        toi=[]
        toj=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                
                # print(matrix[i][j])
                if matrix[i][j]==0:
                    toi.append(i)
                    toj.append(j)
                
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in toi or j in toj:
                    matrix[i][j] = 0

        print(toi)
        print(toj)