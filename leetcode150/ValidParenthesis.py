
class Solution:
    def isValid(self, s: str) -> bool:
        opToCl = { "(" : ")" , "{" : "}" , "[" : "]"}
        read = []
        opSet = set(["(" , "{", "["])
        
        for i in s:
            if i in opSet:
                read.append(i)
            else:
                if len(read) and opToCl[read[-1]] == i:
                    read.pop()
                else:
                    return False
                
        if len(read):
            return False
        else:
            return True
                
            