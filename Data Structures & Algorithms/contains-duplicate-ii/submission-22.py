class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # keep a window of hashset
        window = set()
        # keep l
        l = 0
        if k == 0:
            return False
        # iterate r from 0 to n
        for r in range(len(nums)):
            # return True if nums[r] in window
            if nums[r] in window:
                return True
            # if r - l + 1 == k, remove nums[l] from the hashset
            if r - l + 1 > k:
                window.remove(nums[l])
                l += 1
                # l += 1
            # add nums[r] to window
            window.add(nums[r])
            # print(window)
        return False