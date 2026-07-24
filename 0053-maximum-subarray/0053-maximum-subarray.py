'''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        for i in range(len(nums)):
            temp = 0
            for j in range(i,len(nums)):
                temp = temp + nums[j]
                maxsum = max(maxsum,temp)
        return maxsum'''
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        ms = 0
        for i in range(len(nums)):
            if ms<0:
                ms = 0
            ms+=nums[i]
            maxsum = max(maxsum,ms)
        return maxsum'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum=0
        for i in nums:
            cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum=0
        return max_sum

