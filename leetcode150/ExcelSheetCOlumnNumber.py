# x = "CDA"
# res = 0
# for i in x:
#     res *= 26
#     res += ord(i) - 64

# print(res)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in columnTitle:
            res *= 26
            res += ord(i) - 64

        return res