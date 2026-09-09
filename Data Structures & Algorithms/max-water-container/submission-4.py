class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # keep area count to get min(heights[l], heights[r]) ** 2
        l, r = 0, len(heights)-1
        area = 0
        while l < r:
            area = max(area, min(heights[l], heights[r]) * (r - l))
            # increment l if heights[l] < heights[r]
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            # decrement r if heights[r] <= heights[l]
        return area