class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sort by lambda function 
        points.sort(key=lambda p: (p[0]**2 + p[1]**2)**(1/2))
        return points[:k]
        # # Time: O(n * log(k), Space: O(k)
        # if len(points) == 1:
        #     return points[0]
        
        # # list to return
        # res = []

        # # create a maxheap
        # maxHeap = []
        
        # # store euclidean distance in the max heap -> O(n log k)
        # for x, y in points:
        #     dist = (x**2 + y**2)**(1/2)
        #     heapq.heappush(maxHeap, [-dist, x, y]) # O(log k)
        #     while len(maxHeap) > k: # O(log k)
        #         heapq.heappop(maxHeap)
        
        # # pop k items to append to list to return -> O((n-k) * log n)
        # while maxHeap:
        #     _, x, y = heapq.heappop(maxHeap)
        #     res.append([x, y])

        # return res


        # # -2
        
        # # {2: [[0, 2]]}
        # # {2.82: [[2, 2]]}