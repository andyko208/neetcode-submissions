class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # square each elements in an iteration
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]
        # nums.sort()
        # return nums
        # pointer l, r
        # if nums[l] ** 2 < nums[r] ** 2, r -= 1
        # elif nums[r] < nums[l] ** 2, nums[l], nums[r] = nums[r], nums[l]
        

        # two pointers to make comparisons l, r
        # array to add to from the max value
        l, r = 0, len(nums)-1
        arr = []
        nums = [n**2 for n in nums]
        while l < r:
            if nums[l] <= nums[r]:
                arr.append(nums[r])
                r -= 1
            elif nums[r] <= nums[l]:
                arr.append(nums[l])
                l += 1
        arr.append(nums[l])
        return arr[::-1]