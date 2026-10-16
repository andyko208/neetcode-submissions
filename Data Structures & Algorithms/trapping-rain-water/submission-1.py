class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # accumulate the height as moving each l and r pointers
        l, r = 0, n-1
        maxLeft, maxRight = height[l], height[r]
        total = 0
        # move l pointer to the right if height[l] < height[r], else r to left
        while l < r:
            # keep updating the max of left and right height
            if height[l] < height[r]:
                l += 1
                # trapped water from left is maxLeft - height[i] right is maxRight - height[i]
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]
        return total