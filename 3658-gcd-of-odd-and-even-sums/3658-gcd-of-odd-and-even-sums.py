class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        s,s1=0,0
        if n%2==0 or n%2!=0:
            s = n*(n+1)
            print(s)
            s1= n*n
            print(s1)
        r=math.gcd(s,s1)
        return r


        