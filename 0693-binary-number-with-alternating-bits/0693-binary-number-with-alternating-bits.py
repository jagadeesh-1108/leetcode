class Solution:
    def hasAlternatingBits(self, n: int) -> bool: 
        l=[]
        # n=bin(n)
        while(n!=0):
            r = n % 2
            l.append(r)
            n//=2
        # print(l)
        for i in range(1,len(l)):
            if l[i-1] == l[i]:
                return False
        return True
        