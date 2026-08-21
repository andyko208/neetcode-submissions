class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # # Naive O(N * k) solution
        # # iterate i from 0 to n-k
        # n = len(nums)
        # for i in range(n-1):
        #     # check for each i by iterating from i to i+k whether nums[i] == nums[j]
        #     for j in range(i+1, i+k+1):
        #         if j < n and nums[i] == nums[j]:
        #             return True
        # return False
        # O(N)
        # create a hashmap and store each element with indicies
        # whenever new element is seen, check if that value - k is the previous ind to return True
        n = len(nums)
        mapp = {}
        for i in range(n):
            if nums[i] in mapp and i - k <= mapp[nums[i]]:
                return True
            mapp[nums[i]] = i
        return False
                
        
