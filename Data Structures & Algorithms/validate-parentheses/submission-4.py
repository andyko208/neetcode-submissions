class Solution:
    def isValid(self, s: str) -> bool:
        # create a hashmap that maps close to open
        closeToOpen = {'}': '{', ']': '[', ')': '('}
        # create a stack
        stack = []
        # iterate through s and append all items not in hashmap (opening brackets)
        for i in range(len(s)):
            if s[i] not in closeToOpen:
                stack.append(s[i])
            # if stack is not empty and stack[-1] == hashmap[s[i]], stack.pop()
            elif stack and stack[-1] == closeToOpen[s[i]]:
                stack.pop()
            else:
                # else return False
                return False
        # return True if len(stack) == 0
        return True if not stack else False