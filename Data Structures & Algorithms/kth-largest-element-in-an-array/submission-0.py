class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force - Time: O(n log n), Space: O(1)
        nums.sort()
        return nums[-k]
        # Time: O(n + logk), Space: O(n)
        # turn nums into minHeap
        # pop items while len(minHeap) > k
        # return the first element of minHeap