class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}

        for i in strs:
            sortedi = ''.join(sorted(i))
            # print(sortedi)
            if sortedi not in mp:
                mp[sortedi] = [i]
            else:
                mp[sortedi].append(i)
        
        res = []

        for value in mp.values():
            res.append(value)
        
        return res


                    