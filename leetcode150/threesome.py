class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = []
        z = []
        p = []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        N = set(n)
        P = set(p)

        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        if len(z) >= 3:
            res.add((0,0,0))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                t = -1*(n[i]+n[j])
                if t in P:
                    res.add(tuple(sorted([n[i], n[j], t])))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                t = -1*(p[i]+p[j])
                if t in N:
                    res.add(tuple(sorted([p[i], p[j], t])))

        return res

