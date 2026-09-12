class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push operands to the stack
        stack = []
        opers = {'+', '-', '*', '/'}
        # when operation is seen, pop operands to apply the operation
        for i in range(len(tokens)):
            oper = tokens[i]
            # operation
            if oper in opers:
                rOper = stack.pop()
                lOper = stack.pop()
                if oper == '+':
                    # push back the result back in the stack
                    stack.append(lOper + rOper)
                elif oper == '-':
                    stack.append(lOper - rOper)
                elif oper == '*':
                    stack.append(lOper * rOper)
                elif oper == '/':
                    # print(lOper, rOper, )
                    stack.append(int(lOper / rOper))
            # numbers
            else:
                stack.append(int(oper))
            # print(stack)
        return stack[-1]
        [22]
        