class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l + h) // 2
            # print(nums[l], nums[mid], nums[h])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                h = mid-1
        return -1
        
        # base case: if the value == target, return
        # search(l+1, h) if value is smaller than target
        # search(0, l) if vallue is larger than target
        
        # -1, 4, 8
        # -1, 0, 2
        #  4, 4, 4
        #  4, x, 2