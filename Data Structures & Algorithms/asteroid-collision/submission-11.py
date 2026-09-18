class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # create a stack
        stack = []
        # iterate a in asteroids
        for a in asteroids:
            # while stack and stack[-1] > 0 and a < 0 -> only time when collision happens
            while stack and stack[-1] > 0 and a < 0:
                # get diff = stack[-1] + a
                diff = stack[-1] + a
                # if diff < 0, a wins so pop
                if diff < 0:
                    stack.pop()
                # elif diff > 0, stack[-1] wins so exit without pushing a
                elif diff > 0:
                    a = 0
                # else, pop and exit without pushing a
                else:
                    stack.pop()
                    a = 0
            # push a to stack if a
            if a:
                stack.append(a)
        # return stack
        return stack