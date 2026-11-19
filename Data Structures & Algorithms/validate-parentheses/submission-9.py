class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n) from iterating through
        # Space: O(n) from holding all elements in s
        # define variables
        stack = []
        n = len(s)
        sMap = {')': '(', ']': '[', '}': '{'}
        for i in range(n):
            if s[i] in sMap:
                # check if closing appears before opening
                if stack and sMap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0