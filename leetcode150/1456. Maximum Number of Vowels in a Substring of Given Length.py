class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        first = s[:k]
        count = 0
        maxi = 0
        for c in first:
            if c in vowels:
                count += 1
        maxi = count
        # print(count)
        for i in range(k, len(s)):
            if first[0] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1

            first = first[1:]
            first += s[i]
            maxi = max(count, maxi)

        return maxi
