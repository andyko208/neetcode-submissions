class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select - Time: O(n), Space: O(1)
        # set k
        k = len(nums) - k

        # define a recursive function
        def quickSelect(l, r):
            pivot, p = nums[r], l
            # iterate l from 0 to r
            for i in range(l, r):
                # swap to keep vals <= pivot to its left
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            # swap to place the pivot in the right spot
            nums[p], nums[r] = nums[r], nums[p]
        
            # return right away if kth smallest is found
            if p == k:
                return nums[p]
            # target is on the left side of pivot
            if p > k:
                # recurse on the left
                return quickSelect(l, p - 1)
            # target is on the right side of pivot
            if p < k:
                # recurse on the right
                return quickSelect(p+1, r)
        return quickSelect(0, len(nums)-1)
