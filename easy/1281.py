# [1281] Subtract the Product and Sum Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        
        for dig in str(n):
            product *= int(dig)
            sum += int(dig)
            
        return product - sum