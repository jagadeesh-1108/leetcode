class Solution:
    def reverse(self, x: int) -> int:
        negative=0
        if x<0:
            x = -x
            negative = x
        rev=0
        while x>0:
            digit = x %10
            rev= rev*10 + digit
            x=x//10
        if rev > 2**31 - 1:
            return 0
            
        if negative>0:
            return -(rev)
        return rev
        




        
        
        