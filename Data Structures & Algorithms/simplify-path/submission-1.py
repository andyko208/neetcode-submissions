class Solution:
    def simplifyPath(self, path: str) -> str:
        # slash cannot exist at the end
        # slashes are usually in between the path
        # get all path elements and join with '/'
        # ignore '.'
        # pop when '..'

        # create a stack
        stack = []
        # split path with '/'
        split = path.split('/')
        # iterate through s in split
        for s in split:
            # if s == '..', pop from stack if stack
            if s == '..':
                if stack:
                    stack.pop()
            # if s != '.' and '', push to stack
            elif s != '.' and s != '':
                stack.append(s)
        # return '/' + '/'.join(stack)
        return '/' + '/'.join(stack)