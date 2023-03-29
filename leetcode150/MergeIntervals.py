class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals)==0:
            return res
        elif len(intervals)==1:
            return intervals
        intervals.sort()
        for i in range(len(intervals)):
            if i == 0:
                res.append(intervals[i])
            else:
                # print(res[-1][1])
                # print(intervals[i][1])
                if res[-1][1] >= intervals[i][0]:
                    if intervals[i][1] >= res[-1][1]:
                        res[-1][1] = intervals[i][1]
                    if intervals[i][0] < res[-1][0]:
                        res[-1][0] = intervals[i][0]

                    
                else:
                    res.append(intervals[i])

        return res