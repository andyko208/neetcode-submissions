class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a counter hashmap
        counter = Counter(nums)
        # sort by values and pick the last k elements
        sorted_items = sorted(counter.items(), key=lambda x: x[1])
        # print(sorted_items)
        keys = [num for num, freq in sorted_items[-k:]]
        return keys
        
        