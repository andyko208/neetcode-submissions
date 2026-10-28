class KthLargest:
    # keep k up to k nodes of min heap to return the root for kth largest
    def __init__(self, k: int, nums: List[int]):
        # create a min heap
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # O(N)
        # pop a node until the length of the heap == k
        while len(self.minHeap) > self.k: # O(n-k * log(n))
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        # push val to minHeap
        heapq.heappush(self.minHeap, val) # O(log n)

        # pop node while the number of elements > k
        while len(self.minHeap) > self.k: # O(n-k * log(n))
            heapq.heappop(self.minHeap)

        # return the first element of the minHeap(root)
        return self.minHeap[0]