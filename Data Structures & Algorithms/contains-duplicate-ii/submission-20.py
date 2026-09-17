class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # keep a max of k size set and add nums[i] to it 
        # if size of it goes beyond k, remove the nums[i-k] from the set
        # return true if nums[i] is in the set


        # create a hashset
        if k == 0:
            return False
        window = set()
        n = len(nums)
        # iterate i from 0 through n
        for i in range(n):
            # return True if nums[i] in the set
            if nums[i] in window:
                return True
            # if len(hashset) > k, remove nums[i-k] from the set
            if len(window) == k:
                window.remove(nums[i-k])
            # add nums[i] to the set
            window.add(nums[i])
        return False