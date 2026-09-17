class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # # Brute force
        # n = len(nums)
        # # iterate i from 0 to n-k
        # for i in range(n):
        #     # iterate j from i+1 to i+k+1
        #     window = min(n, i+k+1)
        #     # print(window)
        #     for j in range(i+1, window):
        #         # check for nums[i] == nums[j] to return True
        #         if nums[i] == nums[j]:
        #             return True
        # # return False
        # return False

        # Optimized approach using a hashset
        n = len(nums)
        window = set()
        # iterate i from 0 to n
        for i in range(n):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
        return False
