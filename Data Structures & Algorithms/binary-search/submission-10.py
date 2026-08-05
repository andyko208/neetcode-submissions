class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # think of it as which indicies we should cover
        # keep finding mid and return ind if found
        # otherwise, return -1
        # loop condition such that l and h are valid
        # l, h = 0, len(nums)-1
        # while l <= h:
        #     mid = (l + h) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else:
        #         h = mid -1
        # return -1

        def bsearch(l, h):
            # base case: not found if l < r
            if h < l:
                return -1
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bsearch(mid+1, h)
            else:
                return bsearch(l, mid-1)
        
        l, h = 0, len(nums)-1
        return bsearch(l, h)