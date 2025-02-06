# n = 2
# z = n
# a = z//100
# b = z%100
# print(a, b)
# while True:
#     try:
#         if z == 1:
#             print("true")
#             break
#         if z < 100:
#             a = z//10
#             b = z%10
#         else:
#             a = z//100
#             b = z%100

#         z = a**2 + b**2



#     except:
#         print("false")
#         break

class Solution:
    def isHappy(self, n: int) -> bool:
        z = set()
        while n != 1:
            if n in z:
                return False
            else:
                z.add(n)
                n = sum([int(i)**2 for i in str(n)])
        else:
            return True


