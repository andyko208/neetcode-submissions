class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # define a set to return
        res = []
        
        # try all options and formulate a string
        def dfs(i, word, countO, countC):
            # base case to return if 
            if countO == countC == n:
                # res.add("".join(word))
                res.append("".join(word))
                return
            
            # avoid invalid branches
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
        return res
