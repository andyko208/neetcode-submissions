class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # maintain a window hashset of size k+1
        # return true when size of the window gets smaller than R - L + 1
        L, n = 0, len(nums)
        window = set()
        for R in range(n):
            # adjust the window
            if R - L > k:
                window.remove(nums[L])
                L += 1
            # perform a lookup 
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
