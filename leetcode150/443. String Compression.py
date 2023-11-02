class Solution:
    def compress(self, chars: List[str]) -> int:
        res = ''
        last = ''
        count = 0
        for i in chars:

            if i != last:
                if count > 1:
                    res += str(count)
                res += i
                last = i
                count = 1
            else:
                count += 1
        if count > 1:
            res += str(count)
        # return res
        res = list(res)
        # print(res)
        # return len(res)
        # chars[0] = 'c'
        # print(len(chars))
        # print(len(res))
        # for i in range(0, len(res)):
        #     print(chars)
        # print(chars)

        chars[:] = list(res)
