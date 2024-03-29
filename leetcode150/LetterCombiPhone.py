class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        res = []

        def run(index, currString):
            if index == len(digits):
                res.append(currString)
            else:
                for letter in phone[digits[index]]:
                    run(index+1, currString + letter)

        run(0, '')

        return res