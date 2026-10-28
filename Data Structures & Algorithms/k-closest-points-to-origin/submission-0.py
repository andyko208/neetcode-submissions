class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(n * log(k) + k log(k), Space: O(max(n, k))
        if len(points) == 1:
            return points[0]
        
        # list to return
        res = []
        # hashmap to map {dist: [xi, yi]}
        distToCoord = defaultdict(list)
        # create a maxheap
        maxHeap = []
        heapq.heapify(maxHeap)
        # store euclidean distance in the max heap
        for x, y in points:
            dist = (x**2 + y**2)**(1/2)
            distToCoord[dist].append([x,y])
            heapq.heappush(maxHeap, -dist)
        
        # maintain k items in the heap
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        # pop k items to append to list to return
        while maxHeap:
            val = -heapq.heappop(maxHeap)
            res.extend(distToCoord[val])
            # reset to avoid dup counting
            distToCoord[val] = []

        return res


        # -2
        
        # {2: [[0, 2]]}
        # {2.82: [[2, 2]]}