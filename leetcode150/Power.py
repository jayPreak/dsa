class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        

        def function(base=x, exp = abs(n)):
            if exp == 0:
                return 1
            elif exp % 2 == 0:
                return function(base * base, exp // 2)
            else:
                return base * function(base * base, (exp - 1) // 2)
            
        res = function()
        if n >= 0:
            return float(res)
        else:
            return 1/res

