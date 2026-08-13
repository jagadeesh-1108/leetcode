class Solution:
    def findMin(self, nums: List[int]) -> int:
        # low = 0
        # high = len(nums)-1
        # ans=float('inf')
        # while (low<=high):
        #     mid = (low+high)//2
        #     if nums[low]<=nums[mid]:
        #         if nums[low]<=ans:
        #             ans = nums[low]
        #         low = mid + 1
        #     else:
        #         if nums[mid]<=ans:
        #             ans=nums[mid]
        #         high = mid - 1 
        # return ans

        l=0
        r=len(nums)-1
        while(l<r):
            mid=(l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

                
        