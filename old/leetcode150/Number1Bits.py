# n = 561
# n = str(bin(n)[2:])
# count = 0
# for i in n:
#     if i == "1":
#         count+=1

# print(count)

class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n)[2:])
        c = 0
        for i in n:
            if i == "1":
                c+=1

        return c

        # another sol

        return bin(n).count("1")