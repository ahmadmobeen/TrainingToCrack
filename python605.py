class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        # handle first and last special case
        i = 1
        flowerbed = [0] + flowerbed + [0]
        # while i < len(flowerbed) - 1:
        #     if not flowerbed[i]:
        #         if not flowerbed[i+1]:
        #             flowerbed[i] = 1
        #             count += 1
        #             i += 2
        #     i += 1
        for i in range(1, len(flowerbed) - 1):
            if not flowerbed[i-1] and not flowerbed[i+1]:
                if not flowerbed[i]:
                    count += 1
                    flowerbed[i] = 1
            print(count)
        return count >= n



        # possible = 0
        # prev = 0
        # # if flowerbed[0] == 0 and flowerbed[1] == 0:
        # #     possible += 1
        # #     flowerbed[0] = 1
        # for i in range(1, len(flowerbed) - 1):
        #     if i == 1:
        #         if flowerbed[0] == 0 and flowerbed[i] == 0:
        #             # flowerbed[0] = 1
        #             possible += 1
        #     if i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
        #         possible += 1
        #     if flowerbed[i] != 1:
        #         if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        #             possible += 1 if flowerbed[i] == 0 else possible
        #             flowerbed[i] = 1
        # print(possible)
        # return possible == n
