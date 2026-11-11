class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # # if a car with earlier position gets to target faster than the one with later position, merge them as one because earlier catches and up and considered to be part of the fleet
        # # keep the largest position element with same speed in the stack
        # # create a stack
        # stack = []
        # # create a list of tuple (pos, speed)
        # # cars = [(p, s) for p, s in zip(position, speed)]
        # cars = [(p, s) for p, s in zip(position, speed)]
        # # sort the list sorted
        # cars.sort()
        # # iterate through the list
        # for p, s in sorted(cars):
        #     # time = (target - pos) / speed
        #     t = (target - p) / s
        #     # while stack and (target - stack[-1][0]) / stack[-1][1] <= time, pop from the stack
        #     while stack and (target - stack[-1][0]) / stack[-1][1] <= t:
        #         stack.pop()
        #     # push (pos, speed) to stack
        #     stack.append((p, s))
        # # return len of stack
        # return len(stack)

        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(cars)[::-1]:
            # when does this car reach the target
            t = (target - p) / s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            # print(stack)
        return len(stack)
