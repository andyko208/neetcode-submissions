class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # n1, n2 = 0, 0
        # # iterate until n1 -> len(nums1), n2 -> len(nums2)
        # while n1 < len(nums1) and n2 < len(nums2):
        #     # elif m <= n1 and nums1[n1] == "0", insert nums[n2] there
        #     if m <= n1 and nums1[n1] == 0:
        #         # move the rest elements accordingly
        #         nums1[n1+1:] = nums1[n1:-1]
        #         nums1[n1] = nums2[n2]
        #         n1, n2 = n1+1, n2+1
        #     # n1 += 1 if nums1[n1] < nums2[n2]
        #     elif nums1[n1] < nums2[n2]:
        #         n1 += 1
        #     # elif m > n1 and nums1[n1] > nums[n2], insert nums[n2] there
        #     elif nums2[n2] <= nums1[n1]:
        #         # move the rest elements accordingly
        #         nums1[n1+1:] = nums1[n1:-1]
        #         nums1[n1] = nums2[n2]
        #         n1, n2 = n1+1, n2+1
        m_ptr = m - 1
        n_ptr = n - 1
        k = m + n - 1

        for i in range(k, -1, -1):
            if n_ptr < 0:
                nums1[i] = nums1[m_ptr]
                m_ptr -=1
            elif m_ptr < 0:
                nums1[i] = nums2[n_ptr]
                n_ptr -= 1
            elif nums1[m_ptr] <= nums2[n_ptr]:
                nums1[i] = nums2[n_ptr]
                n_ptr -= 1
            elif nums1[m_ptr] > nums2[n_ptr]:
                nums1[i] = nums1[m_ptr]
                m_ptr -= 1