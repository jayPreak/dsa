class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f = ''
        i = 0
        # longer = 1
        # endappend = 0
        # if len(word1) < len(word2):
        #     longer = 2

        # if longer == 1:
        #     for i in range(0, len(word2)):
        #         f += word1[i]
        #         f += word2[i]
        #         endappend = i + 1
        #     f += word1[endappend:]
        # else:
        #     for i in range(0, len(word1)):
        #         f += word1[i]
        #         f += word2[i]
        #         endappend = i + 1
        #     f += word2[endappend:]

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                f += word1[i]
            if i < len(word2):
                f += word2[i]
            i += 1

        return f
