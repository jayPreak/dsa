class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        lastheight = gain[0]
        maxheight = max(0, gain[0])

        for i in range(1, len(gain)):
            currheight = lastheight + gain[i]
            maxheight = max(maxheight, currheight)
            lastheight = currheight

        return maxheight
