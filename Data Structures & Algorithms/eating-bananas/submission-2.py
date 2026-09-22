import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # get l as 1 and h as max(piles)
        l, r = 1, max(piles)
        min_rate = r
        # while l <= r
        while l <= r:
            # mid = (l + h) // 2
            mid = (l + r) // 2
            # hours = 0
            hours = 0
            # iterate through p in piles
            for p in piles:
                # hours += math.ceil(p / mid)
                hours += math.ceil(p / mid)
            # if hours <= h, min(min_rate, mid), h = mid - 1
            if hours <= h:
                r = mid - 1
                min_rate = min(min_rate, mid)
            # else, l = mid + 1
            else:
                l = mid + 1
            # print(mid, hours, min_rate)
        # return min_rate
        return min_rate
        # [1, 2, 3, 4]