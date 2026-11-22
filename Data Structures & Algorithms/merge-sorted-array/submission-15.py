class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # keep a pointer for merged, one for n1, and for n2
        # compare from the back of each to set value at merged pointer
        # Time: O(n+m) from iterating through both
        # Space: O(1)
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        m, n, i = m-1, n-1, len(nums1)-1
        while i >= 0:
            if m < 0 or n < 0:
                break
            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            elif nums1[m] < nums2[n]:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
        if m < 0 and n >= 0:
            while i >= 0:
                nums1[i] = nums2[n]
                n -= 1
                i -= 1
        elif n < 0 and m >= 0:
            while i >= 0:
                nums1[i] = nums1[m]
                m -= 1
                i -= 1

