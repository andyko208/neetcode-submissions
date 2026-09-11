class MinStack:

    def __init__(self):
        # initialize a list
        self.stack = []
        # keep a min val stack that tells the min stack value for each
        self.min_stack = []


    def push(self, val: int) -> None:
        # append val to list
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
        # print(self.min_stack)
        # compare with min val to update min val


    def pop(self) -> None:
        # pop the list
        self.min_stack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        # return list[-1]
        return self.stack[-1]
        

    def getMin(self) -> int:
        # return self.min_val
        return self.min_stack[-1]
        
