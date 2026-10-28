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
        def dfs(i, word):
            # base case to return 
            if word.count("(") > n or word.count(")") > n:
                return
            if i >= n*2:
                if check(word):
                    res.add("".join(word))
                return
            
            # append parenthesis to word
            word.append("(")
            dfs(i+1, word)
            word.pop()
            word.append(")")
            dfs(i+1, word)
            word.pop()
            # # backtrack
            # dfs(i+1, word)


        dfs(0, [])
        return list(res)