class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search converge the prev element before x if not exists
        n = len(arr)
        l, r = 0, n-1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        print(l, r)

        # adjust l and r so that we are encasing x
        l, r = l - 1, l
        while r - l <= k:
            if l < 0:
                r += 1
            elif r >= n:
                l -= 1
            # smaller val is preferred over bigger if distance is the same
            elif abs(x-arr[l]) <= abs(x-arr[r]):
                l -= 1
            else:
                r += 1
        # l+1 because we want l exclusive, while r already is
        return arr[l+1:r]
        # expand upon the element where binary search returns from  with comparisons