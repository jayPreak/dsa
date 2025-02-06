# m = 3
# n = 7

# # def uniquePaths(m, n):
# #     dp = [[1 for _ in range(n)] for _ in range(m)]
# #     for i in range(1, m):
# #         for j in range(1, n):
# #             dp[i][j] = dp[i-1][j] + dp[i][j-1]             FACKING COPILOT MAN WTF ITS SO BROKEN BUT I WANNA TYPE MYSELF XD
# #     return dp[m-1][n-1]



# def uniquePaths(m, n):
#     dp = [[1 for i in range(n)] for j in range(m)]
#     for i in range(1, m):
#         for j in range(1, n):
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     return dp[m-1][n-1]
# print(uniquePaths(m, n))        WATEVER I DONT CARE ANYMORE OKKK COPILOT IS SO BROKEN huuuuuuuuuuh how r u even guessing what i want to type NAAAAAH MAN THIS IS SO CRAZY bro is learning my vocabulary XD



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return math.comb(1,2)
        dp = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]