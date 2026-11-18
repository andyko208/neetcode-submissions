class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'[': ']', '(': ')', '{': '}'}
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] in mapping and mapping[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            print(stack)
        return len(stack) == 0
