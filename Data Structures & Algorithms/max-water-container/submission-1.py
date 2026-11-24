class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointer keep larger from left and right and move the other

        left, right = 0, len(heights) - 1
        
        maxx = -1
        while left < right:
            maxx = max(maxx, (right - left) * min(heights[left], heights[right]))

            if heights[left] <= heights[right]:
                left += 1
            else:
                right += 1
        
        return maxx