class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a counter of tasks
        counts = Counter(tasks)
        # create maxHeap off of counts
        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)
        # define a queue
        q = deque([])

        # iterate through while q or heap isn't empty
        time = 0
        while maxHeap or q:
            # pop an element from maxHeap
            count = heapq.heappop(maxHeap) if maxHeap else -1
            if count + 1 != 0:
                # add to queue
                q.append((count+1, time+n))
            # pop an element from the queue if valid
            if q and q[0][1] == time:
                taskCount, _ = q.popleft()
                # push to maxHeap
                heapq.heappush(maxHeap, taskCount)
            # print(time, maxHeap, q)
            time += 1
        return time
        # (-2, 4), (-1, 5), (-1, 6), (-1, 8)

        