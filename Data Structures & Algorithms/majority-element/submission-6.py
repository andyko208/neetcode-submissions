class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer moore
        # Time: O(n) from iterating through once
        # Space: O(1)
        # set candidate to nums[0] and count to 1
        # increment count by 1 if nums[i] == candidate, else -=1
        # if count == 0, candidate = nums[i], count += 1
        # return candidate
        # nums.sort()
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if candidate == num:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count = 1
        return candidate