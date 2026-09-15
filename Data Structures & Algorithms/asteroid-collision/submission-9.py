class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # keep a stack
        stack = []
        popped = False
        # iterate a in asteroids
        for a in asteroids:
            # collision happens only when a < 0 and stack[-1] > 0
            while stack and a < 0 and stack[-1] > 0:
                diff = stack[-1] + a
                # if diff < 0, a wins, so pop from the stack
                if diff < 0:
                    stack.pop()
                # elif diff > 0, stack wins, so exit the loop
                elif diff > 0:
                    popped = True
                    break
                # else, both get destroyed, pop from the stack and exit the loop        
                else:
                    popped = True
                    stack.pop()
                    # a = 0
                    break

            # skip pushing to stack if 
            if not popped:
                stack.append(a)
            else:
                popped = False
        return stack