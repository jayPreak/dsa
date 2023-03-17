class Solution:
    def countAndSay(self, n: int) -> str:
        out = "1"

        for i in range(2, n+1):
            res = ""
            curr = out[0]
            count = 1
            for x in out[1:]:
                if x==curr:
                    count+=1
                else:
                    res+=str(count) + curr
                    count = 1
                    curr = x

            res += str(count) + curr
            out = ''.join(res)
        return out

