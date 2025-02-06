class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        chosen = []

        def explore(chosen, remaining, res):
            if not remaining:
                res.append(chosen[:])
                return
            d = remaining.pop(0)
            chosen.append(d)
            explore(chosen, remaining, res)
            chosen.pop()
            explore(chosen, remaining, res)
            remaining.insert(0, d)

        explore(chosen, nums, res)
        return res
        