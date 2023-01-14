# def isPalindrome(s):
#     return s == s[::-1]

# s = "0P"
# s1="".join(c for c in s if c.isalpha())

# print(s1)

# ans = isPalindrome(s1.lower())
# print(ans)
 
# if ans:
#     print("Yes")
# else:
#     print("No")

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]