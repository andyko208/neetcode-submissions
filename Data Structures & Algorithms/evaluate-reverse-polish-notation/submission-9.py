class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # always push numbers to the stack
        # create a stack
        stack = []
        # create hashset of operations
        opers = {'+', '-', '*', '/'}
        # when an operand is seen, pop first for right and another for left operand
        # iterate through tokens
        for i in range(len(tokens)):
            oper = tokens[i]
            # print(oper)
            if oper in opers:
                rOper, lOper  = stack.pop(), stack.pop()
                # res = 0
                # check if tokens[i] is one of the operands
                # if '+', perform add
                if oper == '+':
                    # push the result back to the stack
                    res = lOper + rOper
                # elif '-', perform subtract
                elif oper == '-':
                    # push the result back to the stack
                    res = lOper - rOper
                # elif '*', perform multi
                elif oper == '*':
                    # push the result back to the stack
                    res = lOper * rOper
                # elif '/', perform divi
                elif oper == '/':
                    # push the result back to the stack
                    res = lOper / rOper
                print(res)
                stack.append(int(res))
            # else, push tokens[i] to the stack as an int
            else:
                stack.append(int(oper))
        # return the last element 
        return stack[-1]
        
        # [1, 2] "+" -> 1 + 2 = 3 -> [3]
        # [3, 3] "*" -> 3 * 3 = 9 -> [9]
        # [9, 4] "-" -> 9 - 4 = 5 -> [5]
        # return [5]