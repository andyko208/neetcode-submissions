class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # Brute force
        # n = len(temperatures)
        # # create res of [0] * n
        # res = [0] * n
        # # iterate i from 0 to n
        # for i in range(n):
        #     # iterate j from i + 1 to n
        #     for j in range(i+1, n):
        #     # check if temperatures[j] > temperatures[i] to set res[i] = j - i
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res
        # Optimized monotonic stack approach
        n = len(temperatures)
        # res of 0 * n
        res = [0] * n
        # stack to hold values
        stack = []
        # iterate i from 0 to n
        for i in range(n):
            # if stack and if temp[i] > stack[-1], update res[i-1] to i - ind and append as (temp[i], i)
            while stack:
                val, ind = stack[-1]
                if temperatures[i] > val:
                    res[ind] = i - ind
                    stack.pop()
                else:
                    break
            stack.append((temperatures[i], i))
            # print(stack, res)
        return res
