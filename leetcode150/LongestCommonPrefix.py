# s = ["aa","aa","aazab","aabb"]
# s.sort()
# print(s)
# end = min(len(s[0]), len(s[-1]))

# i=0
# while (i < end and s[0][i] == s[-1][i]):
#     i+=1

# longest = s[0][0:i]
# print(longest)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        end = min(len(strs[0]), len(strs[-1]))
        
        i = 0
        while(i < end and strs[0][i] == strs[-1][i]):
            i+=1
            
        ans = strs[0][0:i]
        
        return ans
        