class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # define a list to return
        valids = []
        # define a recursive function to return 
        def dfs(word, numOpen, numClose):
            # base case to add word to valids
            if numOpen == numClose == n:
                valids.append("".join(word))
                return 
            # adding the opening 
            if numOpen < n:
                word.append("(")
                dfs(word, numOpen+1, numClose)
                word.pop()
            # adding the opening 
            if numClose < numOpen:
                word.append(")")
                dfs(word, numOpen, numClose+1)
                word.pop()
        dfs([], 0, 0)
        return valids
