class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distFn = lambda x: x[0] ** 2 + x[1] ** 2

        def quickSelect(l, r):
            target = k - 1
            while True:
                pivot, p = distFn(points[r]), l

                for i in range(l, r):
                    if distFn(points[i]) <= pivot:
                        points[i], points[p] = points[p], points[i]
                        p += 1

                points[p], points[r] = points[r], points[p]

                if target < p:
                    r = p - 1
                elif target > p:
                    l = p + 1
                else:
                    return

        if k == len(points):
            return points

        quickSelect(0, len(points) - 1)
        return points[:k]