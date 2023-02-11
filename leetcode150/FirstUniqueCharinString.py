class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        # index = -1
        for i in range(len(s)):
            if m[s[i]] == 1:
                return i
        return -1