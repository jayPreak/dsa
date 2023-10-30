class Solution:
    def reverseVowels(self, s: str) -> str:
        # indexes = []
        # vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        # mine = []

        # for i in range(len(s)):
        #     if s[i] in vowels:
        #         indexes.append(i)
        #         mine.append(s[i])

        # print(indexes)
        # print(mine)
        # templist = list(s)
        # i = 0
        # j = -1
        # while i < len(indexes):
        #     templist[indexes[i]] = mine[j]
        #     i += 1
        #     j -= 1

        # res = "".join(templist)
        # # print(templist)
        # return res

        s = list(s)
        res = ''
        vowels = set('aAeEiIoOuU')
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        s = ''.join(s)
        return s
