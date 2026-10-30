class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get the counts of tasks
        # {"X": 2, "Y": 2}
        # [-2, -2]
        
        # t = 0 -> maxHeap[-2], queue: [(3, -1)]
        # t = 1 -> maxHeap[], queue: [(3, -1), (4, -1)]
        # t = 2 -> maxHeap[], queue:[(3, -1), (4, -1)]
        # t = 3 -> maxHeap[-1], queue: [(4, -1)]
        # t = 4 -> maxHeap[-1], queue: []
        # t = 5 -> maxHeap[], queue: []

        # create a count of tasks and turn into a maxHeap
        taskMap = Counter(tasks)
        maxHeap = [-c for c in taskMap.values()]
        heapq.heapify(maxHeap)

        t = 0
        q = deque([])
        # loop to iterate through to continue until we exhaust all tasks
        while maxHeap or q:
            t += 1
            # pop from maxHeap and add to q if possible
            if maxHeap:
                cur = heapq.heappop(maxHeap)
                if cur + 1 <= -1:
                    q.append((t + n, cur+1))
                
            # check if we can pop from the queue to push to maxHeap
            if q and q[0][0] == t:
                _, count = q.popleft()
                heapq.heappush(maxHeap, count)
        return t

# t=0 [-1, -1] [(5, -2)]
# t=1 [-1] [(5, -2)]
# t=2 [] [(5, -2)]
# t=3 [] [(5, -2)]
# t=4 [] [(5, -2)]
# t=5 [-2] []
# t=6 [] [(9, -1)]
# t=7 [] [(9, -1)]
# t=8 [] [(9, -1)]
# t=9 [-1] []
# t=10 [] []
