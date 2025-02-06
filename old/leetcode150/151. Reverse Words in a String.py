class Solution:
    def reverseWords(self, s: str) -> str:

        # def reverseL(lst):
        #     newlst = lst[::-1]
        #     return newlst
        # def removeS(s):
        #     return s.replace(" ", "")
        # words = []
        # lastspace = 0

        # for i in range(len(s)):
        #     if s[i] == ' ':
        #         words.append(s[lastspace:i])
        #         lastspace = i
        # words.append(s[lastspace:])
        # words = reverseL(words)

        # i=0
        # print('before', words)
        # while i < len(words):
        #     print('words r', words[i])
        #     if words[i] == ' ' or words[i] == '':
        #         words.pop(i)
        #         print('hii', i)
        #     else:
        #         words[i] = removeS(words[i])
        #         i+=1

        # print(words)
        # res = ' '.join(words)
        # return res

        words = []
        temp = ''
        for c in s:
            if c != ' ':
                temp += c
            elif temp != '':
                words.append(temp)
                temp = ''

        if temp != '':
            words.append(temp)

        return ' '.join(words[::-1])
