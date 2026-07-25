class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2 = 0, 0
        # iterate until n1 -> len(nums1), n2 -> len(nums2)
        while n1 < len(nums1) and n2 < len(nums2):
            # elif m <= n1 and nums1[n1] == "0", insert nums[n2] there
            if m <= n1 and nums1[n1] == 0:
                # move the rest elements accordingly
                nums1[n1+1:] = nums1[n1:-1]
                nums1[n1] = nums2[n2]
                n1, n2 = n1+1, n2+1
            # n1 += 1 if nums1[n1] < nums2[n2]
            elif nums1[n1] < nums2[n2]:
                n1 += 1
            # elif m > n1 and nums1[n1] > nums[n2], insert nums[n2] there
            elif nums2[n2] <= nums1[n1]:
                # move the rest elements accordingly
                nums1[n1+1:] = nums1[n1:-1]
                nums1[n1] = nums2[n2]
                n1, n2 = n1+1, n2+1
            # else:
            #     print(n1, n2, nums1)
            #     n1, n2 = n1+1, n2+1
            # print(n1, n2)
            # [-10, -5, -2, 0, 0, 0, 0]   n1=1, n2=0
            # [-10, -9, -5, -2, 0, 0, 0]  n1=1, n2=1
            # [-10, -9, -5, -2, 0, 0, 0]  n1=2, n2=2
            # [-10, -9, -5, -2, 0, 0, 0]  n1=3, n2=1
            # [-10, -9, -5, -4, -2, 0, 0]  n1=3, n2=2
            # [-10, -9, -5, -4, -3, -2, 0]  n1=4, n2=3
            # [-10, -9, -5, -4, -3, -2, 0]  n1=5, n2=3
            # [-10, -9, -5, -4, -3, -2, 0]  n1=6, n2=3



        