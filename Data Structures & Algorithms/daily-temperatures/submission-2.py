class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # keep a stack
        stack = []
        # keep n
        n = len(temperatures)
        # res of n 0s
        res = [0] * n
        # iterate i through n
        for i in range(n):
            # while stack and temperatures[stack[-1]] < temperaetures[i]:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # prev = stack.pop()
                prev = stack.pop()
                # res[prev] = i - prev
                res[prev] = i - prev
            # append i to stack
            stack.append(i)
        # return res
        return res