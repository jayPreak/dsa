class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i = 0
        # temp = ''
        # copys = s

        # if t == '' and s == '':
        #     return True

        # while i < len(t):
        #     if temp == s:
        #         return True
        #     if copys[0] == t[0]:
        #         temp += copys[0]
        #         if temp == s:
        #             return True
        #         t = t[1:]
        #         copys = copys[1:]
        #     else:
        #         t = t[1:]
        # return False

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        else:
            return False
