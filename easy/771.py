# [771] Jewels and Stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        
        for char in S:
            if char in list(J):
                count += 1
                
        return count