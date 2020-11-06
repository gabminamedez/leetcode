# [1480] Running Sum of 1D Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new = [nums[0]]
        curr = new[len(new) - 1]
        for i in range (1, len(nums)):
            curr = new[len(new) - 1]
            new.append(nums[i] + curr)
            
        return new