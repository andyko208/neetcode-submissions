class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack
        stack = []
        # create a set of opening chars
        opens = {'(', '{', '['}
        # create a set of closing chars
        closes = {')', '}', ']'}

        # iterate through s
        for i in range(len(s)):
        # check if s[i] is in opening chars, append it
            if s[i] in opens:
                stack.append(s[i])
            # check if s[i] is in closing chars, check if it matches with stack[-1]
            elif s[i] in closes and len(stack) > 0:
                # if matching, pop stack[-1]
                if s[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif s[i] == ']' and stack[-1] == '[':
                    stack.pop()
                # if not matching chars, return False
                else:
                    return False
            else:
                return False
        # return True
        return True if len(stack) == 0 else False