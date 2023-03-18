
#my coeedee
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        #distribut money to children but result needs to be the maximum number of children who get 8 dollars, but all children need to get 1 dollar but not 4 dollars
        if money < children:
            return -1
        child = [1] * children
        money -= children
        i = 0
        while money != 0:
            if i>children-1:
                break
            if money>=7:
                child[i] += 7
                money -= 7
                i+=1
            else:
                break
        # print(child)
        result = child.count(8)
        onescount = child.count(1)
        if money == 3 and result == 0:
            return result
        elif money == 3 and onescount ==1:
            return result -1
        elif result == children and money >0:
            return result -1
        else:
            return result
                
                    


#chatgpt's code
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # if there is not enough money to give each child at least 1 dollar
        if money < children:
            return -1
        
        # initialize each child with 1 dollar
        child = [1] * children
        
        # subtract the total amount of dollars given to children from the total amount of money
        money -= children
        
        i = 0
        # distribute 7 dollars to each child until there is not enough money left to give another 7 dollars
        while money >= 7 and i < children:
            child[i] += 7
            money -= 7
            i += 1
        
        # count the number of children who received 8 dollars
        result = child.count(8)
        
        # count the number of children who received 1 dollar
        onescount = child.count(1)
        
        # check for special case where 3 dollars are left and no child received 8 dollars
        if money == 3 and result == 0:
            return result
        
        # check for special case where 3 dollars are left and only one child received 1 dollar
        elif money == 3 and onescount == 1:
            return result - 1
        
        # check for special case where all children received 8 dollars but there is still money left
        elif result == children and money > 0:
            return result - 1
        
        # return the number of children who received 8 dollars
        else:
            return result

        