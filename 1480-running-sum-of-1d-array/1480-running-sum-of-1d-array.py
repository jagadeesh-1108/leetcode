class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        total=0
        for i in nums:
            total=total+i
            res.append(total)
        return res
        