class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = (high-low)+1
        half = total//2
        if total%2!=0:
            if low%2!=0 and high%2!=0:
                return half+1
            else:
                return half
        else:
            return half
        