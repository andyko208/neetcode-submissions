class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force - Time: O(n log n), Space: O(1)
        # nums.sort()
        # return nums[-k]

        # min heap - Time: O(n + logk), Space: O(n)
        # turn nums into minHeap
        heapq.heapify(nums)
        # pop items while len(minHeap) > k
        while len(nums) > k:
            heapq.heappop(nums)
        # return the first element of minHeap
        return nums[0]