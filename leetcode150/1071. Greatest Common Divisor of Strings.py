class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       # res = ""
        # longer = 1
        # if len(str1) < len(str2):
        #     longer = 2

        # if longer == 1:
        #     if str2 in str1:
        #         i = 0
        #         temp = str1
        #         while i < len(str2):
        #             if str1[i] == str2[i]:
        #                 temp = temp[1:]
        #                 temp = temp[:-1]
        #             else:
        #                 res = temp
        #             i+=1
        #     else:
        #         return res
        # else:
        #     if str1 in str2:
        #         i=0
        #         while i < len(str2):
        #             if str2[i] == str1[i]:
        #                 str2 = str2[1:]
        #             else:
        #                 res += str2[i]
        #                 str2 = str2[1:]
        #             i+=1

        #     else:
        #         return res

        # return res

        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            print("n1, n2 are", n1, n2)
            base = str1[:k]
            print("base", base)
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            print("i is", i)
            if valid(i):

                return str1[:i]
        return ""
