class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # keep a stack with a pointer at the last index
        # iterate through operations 
        stack, ind = [], 0
        for op in operations:
            if op == "+":
                stack.append(int(stack[ind-1]) + int(stack[ind-2]))
                ind += 1
            elif op == "D":
                stack.append(int(stack[ind-1]) * 2)
                ind += 1
            elif op == "C":
                stack.pop()
                ind -= 1
            else:
                stack.append(int(op))
                ind += 1
            print(stack)
        return sum(stack)