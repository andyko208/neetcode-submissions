class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a counter hashmap
        counter = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for n, c in counter.items():
            freq[c].append(n)
        # iterate through freq and get the top two most frequent
        res = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i]:
                res.extend(freq[i])
            if len(res) == k:
                break
        return res
        