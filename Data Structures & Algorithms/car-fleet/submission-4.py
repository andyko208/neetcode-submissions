class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # fleet is based on the POSITION and SPEED
        # sort by position of each cars in dec order
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort()
        # keep checking if prev stack has speed <= curr to skip over pushing to the stack
        stack = []
        for p, s in cars:
            # get the time
            time = (target - p) / s
            # check the last two items in the stack and compare time to pop the shortest time element
            while stack and (target - stack[-1][0]) / stack[-1][1] <= time:
                stack.pop()
            stack.append((p, s))
            # print(stack)
        return len(stack)