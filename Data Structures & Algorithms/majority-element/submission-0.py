class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # simple way is to sort and find the middle element since appearing more than n/2 times guarantees it being there
        nums.sort()
        return nums[len(nums)//2]