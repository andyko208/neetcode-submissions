class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # simple way is to sort and find the middle element since appearing more than n/2 times guarantees it being there -> Time: O(N log N), Space: O(1)
        # nums.sort()
        # return nums[len(nums)//2]

        # # Optimal approach: create a hashamp and find key of values > n / 2
        # counter = Counter(nums) # Time: O(N), Space: O(N)
        # n = len(nums)
        # for num, count in counter.items():
        #     if count > n // 2:
        #         return num
        # return 0

        # keep a highest value counter and element as we iterate through nums
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate != num:
                count -= 1
            else:
                count += 1
        return candidate