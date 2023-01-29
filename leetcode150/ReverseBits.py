# x = 43261596
# x = bin(x)[2:]
# x = x.zfill(32)
# print(x.zfill(32))
# a = "".join(reversed(x))
# print(int(a, 2))

class Solution:
    def reverseBits(self, n: int) -> int:
        n = "".join(reversed(str(bin(n)[2:].zfill(32))))
        return int(n, 2)