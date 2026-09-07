class NumArray:

    def __init__(self, nums: List[int]):
        # [0, -2, -2, 1, -4, -2, -3]
        # [0, -2, -2, 1, -4, -2, -3]
        # create a prefix sum array with 0 as the first element
        n = len(nums)
        prefixSum = [0] * (n+1)
        curSum = 0
        for i in range(n):
            curSum += nums[i]
            prefixSum[i+1] += curSum
        self.prefixSum = prefixSum
        # print(self.prefixSum)

    def sumRange(self, left: int, right: int) -> int:
        # query to get the difference between the prefixsum array of arr[r+1] - arr[l]
        return self.prefixSum[right+1] - self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)