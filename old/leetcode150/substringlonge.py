class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        curr = set()
        for i in range(len(s)):
            curr.clear()
            j = i
            while j < len(s):
                if s[j] in curr:
                    break
                curr.add(s[j])
                j+=1
            res = max(res, j - i)

        return res