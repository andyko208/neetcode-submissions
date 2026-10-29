class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n + (n-k)log n), Space: O(n)
        # turn nums into minHeap
        heapq.heapify(nums)

        # pop items until we're left with k elements
        while len(nums) > k:
            heapq.heappop(nums)
        # return the root node of the minHeap
        return nums[0]
