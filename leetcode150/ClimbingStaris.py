# n = int(input())

# if n == 0 or n == 1 or n == 2:
#     print(n)
# else:
#     one = 2
#     two = 1
#     total = 0
#     for i in range(3, n+1):
#         total = one + two
#         two = one
#         one = total

#     print(total)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        else:
            one = 2
            two = 1
            total = 0
            for i in range(3, n+1):
                total = one + two
                two = one
                one = total
            return total