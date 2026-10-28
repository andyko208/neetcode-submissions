class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # define a set to return
        res = set()

        # helper funciton to check whether the string is well-formed
        def check(word):
            # create a stack
            stack = []
            # iterate through c in word
            for c in word:
                # check if it's valid to remove or pop
                if c == ")" and stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
            return True if len(stack) == 0 else False
        
        # try all options and formulate a string
        def dfs(i, word, countO, countC):
            # base case to return if 
            if countO == countC == n:
                res.add("".join(word))
                return
            
            if countO < n:
                # append parenthesis to word
                word.append("(")
                dfs(i+1, word, countO+1, countC)
                # backtrack
                word.pop()
            if countC < countO:
                word.append(")")
                dfs(i+1, word, countO, countC+1)
                # backtrack
                word.pop()

        dfs(0, [], 0, 0)
        return list(res)
