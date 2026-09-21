class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # keep a pointer k that starts from m+n-1
        k = m + n - 1
        # keep pointer n1 and n2 for each nums1 and nums2
        n1, n2 = m-1, n-1
        # loop while one of n1 or n2 has reached the end
        while 0 <= n2:
            # compare nums[n1] and nums[n2] to assign to nums1[m+n-1]
            if 0 <= n1 and nums1[n1] > nums2[n2]:
                nums1[k] = nums1[n1]
                # decrement n1 or n2 by 1 after each assignment
                n1 -= 1
            else:
                nums1[k] = nums2[n2]
                n2 -= 1
            k -= 1
        # # push the remaining n1 pointer to the end
        # while 0 <= n1:
        #     nums1[k] = nums1[n1]
        #     n1, k = n1-1, k-1
        # # push the remaining n2 pointer to the end
        # while 0 <= n2:
        #     nums1[k] = nums2[n2]
        #     n2, k = n2-1, k-1
