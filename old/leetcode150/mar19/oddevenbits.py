a = 17
res = [0, 0]
bin_a = bin(a)
print(bin_a)
bin_a = bin_a[2:]
bin_a = bin_a[::-1]
print(bin_a)
print(type(bin_a))
for i in range(len(bin_a)):
    print(i)
    if bin_a[i] == '1' and i % 2 == 0:
        print('even')
        res[0] += 1

    elif bin_a[i] == '1' and i % 2 == 1:
        print('odd')
        res[1] += 1
    print('---')



print(res)


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0, 0]
        bin_n = bin(n)
        bin_n = bin_n[2:]
        bin_n = bin_n[::-1]
        for i in range(len(bin_n)):
            if bin_n[i] == '1' and i % 2 == 0:
                res[0] += 1
            elif bin_n[i] == '1' and i % 2 == 1:
                res[1] += 1
        
        if n==1:
            return [1,0]
        elif n==2:
            return [0,1]
        else:
            return res
    