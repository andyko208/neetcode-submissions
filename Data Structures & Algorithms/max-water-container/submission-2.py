class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount = (r - l) * max(heights[r], heights[l])
        # while l < r, l += 1 if nums[l] <= nums[r], r += 1 otherwise
        amount = 0
        l, r = 0, len(heights)-1
        while l < r:
            amount = max((r - l) * min(heights[l], heights[r]), amount)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        return amount