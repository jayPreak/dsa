class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        res = 0
        y = ord("a")-1
        if s == chars and sum(vals)<0:
            return res
        else:
            for i in range(len(s)):
                for j in range(i, len(s)+1):
                    temp = 0
                    # print(i, "yep", j)
                    # print(s[i:j])
                    for x in s[i:j]:
                        
                        if x in chars:
                            temp += vals[chars.index(x)]
                        else:
                            temp+= ord(x) - y
                    res = max(res, temp)
                    
            return res
                    