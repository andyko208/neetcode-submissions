class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # x may or may not exist in arr
        # goal is to find k integers from arr that is the most closest than other elements in arr
        # smaller value is preferred over the bigger than x

        n = len(arr)
        l = 0
        res = []
        # add elements from the right
        for r in range(n):
            # our current window size went beyond
            while r - l + 1 > k:
                # remove left is right is closer
                if abs(arr[r] - x) < abs(arr[l] - x):
                    l += 1
                elif arr[r] == arr[l]:
                    l += 1
                # if l is closer, then we've found the right set
                else:
                    return arr[l:r]

        return arr[l:r+1]


        # remove elements from the left as long as the element on the right is closer to x
        # the first time we stop removing left is a potential final arr