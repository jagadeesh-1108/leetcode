class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = (high - low)+1
        if total%2==0:
            total = total//2
        elif total%2!=0 and (low%2!=0 and high%2!=0):
            total=(total//2)+1
        elif total%2!=0 and(low%2==0 and high%2==0):
            total//=2
        return total
            
        