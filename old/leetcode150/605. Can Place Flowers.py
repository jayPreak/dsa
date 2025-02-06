class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # i = 0
        # if len(flowerbed)>1:
        #     if flowerbed[0] == 0 and flowerbed[1] == 0:
        #         n -= 1
        #         flowerbed[0] = 1
        #     if flowerbed[-2] == 0 and flowerbed[-1] == 0:
        #         n-=1
        #         flowerbed[-1] = 1
        #     for i in range(1, len(flowerbed)-1):
        #         if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
        #             n -= 1
        #             flowerbed[i] = 1
        # else:
        #     if flowerbed[0] == 0:
        #         n-=1

        # if n <= 0:
        #     return True
        # else:
        #     return False

        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False
