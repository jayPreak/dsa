class Solution:
    def reverse(self, x: int) -> int:
        # print(x)
        r = int(str(abs(x))[::-1])

        if r.bit_length() > 31:
            return 0

        if x<0:
            return -1*r
        else:
            return r