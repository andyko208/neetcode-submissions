class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        # turn nums into a min heap
        heapq.heapify(nums)
        # pop from the min heap while there are more elements than k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # add val to heap
        heapq.heappush(self.minHeap, val)
        # pop the smallest while the length of the heap is greater than k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        