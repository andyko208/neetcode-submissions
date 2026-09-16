class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # create res of [0] * (n+1)
        res = [0] * (n+1)
        # set res[-1] to -1
        res[-1] = -1
        # iterate from n-2 to get the max of max_count and arr[i]
        for i in range(len(res)-2, -1, -1):
            res[i] = max(arr[i], res[i+1])
        # return res[1:]
        # print(res)
        return res[1:]