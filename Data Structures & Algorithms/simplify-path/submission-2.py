class Solution:
    def simplifyPath(self, path: str) -> str:
        # split path by '/'
        split = path.split('/')
        # keep a stack
        stack = []
        # iterate s in split
        for s in split:
            # if s == '..', pop from stack
            if s == '..':
                if stack:
                    stack.pop()
            # elif s is valid, not '.' nor '', push to stack
            elif s != '.' and s != '':
                stack.append(s)
        # join stack as '/' with '/' prepended
        return '/' + '/'.join(stack)