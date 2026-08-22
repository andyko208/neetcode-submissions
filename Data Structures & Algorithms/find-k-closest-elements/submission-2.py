class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # x may or may not exist in arr
        # goal is to find k integers from arr that is the most closest than other elements in arr
        # smaller value is preferred over the bigger than x

        # n = len(arr)
        # l = 0
        # res = []
        # # add elements from the right
        # for r in range(n):
        #     # our current window size went beyond
        #     while r - l + 1 > k:
        #         # remove left is right is closer
        #         if abs(arr[r] - x) < abs(arr[l] - x):
        #             l += 1
        #         elif arr[r] == arr[l]:
        #             l += 1
        #         # if l is closer, then we've found the right set
        #         else:
        #             return arr[l:r]
        # # if we didn't return earlier, we've include all the set
        # return arr[l:r+1]

        # find the leftmost position
        n = len(arr)
        l, r = 0, n-1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        l, r = l - 1, l
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                l -= 1
            else:
                r += 1
        print(l, r)
        return arr[l+1:r]