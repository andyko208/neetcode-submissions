class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # create a counter hashmap of arr
        counter = Counter(arr)
        distincts = 0
        # iterate through arr and check if counter[arr[i]] == 1, increment distinct count by 1
        for i in range(len(arr)):
            if counter[arr[i]] == 1:
                distincts += 1
            if distincts == k:
                return arr[i]
        # if distinct count == k, return arr[i], else ""
        return ""