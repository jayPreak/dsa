# print(3<<1)
# # print(7^-3)

# print(1<<1)
# # print(abs(-3))

# print(7 - (3<<1))

# # sign = +1 if 

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = +1 if dividend ^ divisor >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)

        ans = 0

        for power in range(31, -1, -1):
            if (divisor << power) <= dividend:
                ans += (1<<power)
                dividend -= (divisor << power)

        ans = 0 - ans if sign == -1 else ans

        if not (-2**31 <= ans <= 2**31-1):
            ans = 2**31 -1

        return ans     