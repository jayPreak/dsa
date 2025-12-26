# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         a = int("".join(map(str, digits)))
#         a += 1
#         digits = list(map(int, str(a)))
#         return digits
                
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        while True:
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                print(f'i: {i}')
                print(f'0: {digits[0]}, digits i: {digits[i]}')
                if digits[0] == digits[i]:
                    digits[i] = 0
                    meow = len(digits)*-1
                    print(f'digits : {digits}, len(digits): {meow} AND i = {i}')
                    if len(digits) * -1 == i:
                        digits.insert(0, 1)
                        break 
                    i-=1
                else:
                    digits[i] = 0
                    if len(digits) * -1 == i:
                        break
                    i -= 1
                    
                    
                    
        print(digits)
        return digits
                    
                    
        