class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # simple way is to sort and find the middle element since appearing more than n/2 times guarantees it being there -> Time: O(N log N), Space: O(1)
        # nums.sort()
        # return nums[len(nums)//2]

        # Optimal approach: create a hashamp and find key of values > n / 2
        counter = Counter(nums)
        n = len(nums)
        for num, count in counter.items():
            if count > n // 2:
                return num
        return 0

