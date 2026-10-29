class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # quick select
        distFn = lambda x: x[0] ** 2 + x[1] ** 2
        # define a function called quickSelect
        def quickSelect(l, r):
            while True:
                # set pivot and p index
                pivot, p = distFn(points[r]), l
                # iterate i from l to r
                for i in range(l, r):
                    # check if distance of points at i is smaller than equal to pivot
                    if distFn(points[i]) <= pivot:
                        points[i], points[p] = points[p], points[i]
                        # increment pivot index
                        p += 1
                # swap points at r with points at p
                points[p], points[r] = points[r], points[p]
            
                # check if k < p, recurse on left
                if k-1 < p:
                    r = p-1
                elif k-1 > p:
                    l = p + 1
                else:
                    break
        quickSelect(0, len(points)-1)

        return points[:k]