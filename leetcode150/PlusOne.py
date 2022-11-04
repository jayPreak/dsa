class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int("".join(map(str, digits)))
        a += 1
        digits = list(map(int, str(a)))
        return digits
                
                