# [1470] Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n1 = 0
        n2 = n
        
        new = []
        for i in range(n):
            new.append(nums[n1])
            new.append(nums[n2])
            n1 += 1
            n2 += 1
            
        return new