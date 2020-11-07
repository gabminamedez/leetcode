# [1431] Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        currMax = max(candies)
        candies = [candy + extraCandies for candy in candies]
        
        bools = []
        for i in range(len(candies)):
            if candies[i] >= currMax:
                bools.append(True)
            else:
                bools.append(False)
                
        return bools