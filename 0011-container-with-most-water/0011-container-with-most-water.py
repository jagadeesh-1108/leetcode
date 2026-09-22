class Solution:
    def maxArea(self, height: list[int]) -> int:
        # h=len(height)
        # base=0
        # max_area=0
        # for i in range(h):
        #     for j in range(h):
        #         base = j-i
        #         a = min(height[i],height[j])
        #         area= a * base
        #         if max_area<area:
        #             max_area=area
        # return max_area
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            base= right-left
            h = min(height[left],height[right])
            area = h * base
            max_area=max(max_area,area)
            if height[left]< height[right]:
                left+=1
            else:
                right-=1
        return max_area


