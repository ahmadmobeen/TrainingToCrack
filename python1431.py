class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        result = [False] * len(candies)
        print(result)
        for i in range(len(candies)):
            greatest = candies[i] if candies[i] > greatest else greatest
        print(greatest)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= greatest:
                result[i] = True
        return result
