# Using Two Pointer Technique
class Solution(object):
    def maxArea(self, height):
        
        left = 0
        right = len(height) - 1
        max_area = 0


        while left < right:
            area = (right - left) * min(height[right], height[left])
            max_area = max(max_area, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area


