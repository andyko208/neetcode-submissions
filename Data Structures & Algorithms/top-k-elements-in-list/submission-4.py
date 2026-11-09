class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n), Space: O(n)
        # define variables
        n = len(nums)
        # create a list of empty list of size n+1, each index represents the count
        buckets = [[] for _ in range(n+1)]
        # a list to return
        topK = []
        # get the count of elements in nums
        numCounter = Counter(nums)
        # put the count as index of the bucket for the element
        for num, freq in numCounter.items():
            buckets[freq].append(num)
        # iterate from the back and append the element to list to return
        for i in range(len(buckets)-1, -1, -1):
            # include all elements in the current bucket
            topK.extend(buckets[i])
            if len(topK) == k:
                return topK