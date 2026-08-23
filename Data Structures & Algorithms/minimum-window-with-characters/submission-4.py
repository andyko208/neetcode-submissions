class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time: O(N), Memory: O(N)
        # If t is empty, return "".
        if not t:
            return ""
        
        # Build a frequency map countT for characters in t.
        countT, window = Counter(t), Counter()

        # have and need, res and resLen
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l, n = 0, len(s)

        # loop through r
        for r in range(n):
            # Add s[r] to window.
            window[s[r]] += 1

            # If s[r] is in countT and its count in window matches countT, increment have.
            if countT[s[r]] == window[s[r]]:
                have += 1
            # window is valid
            while have == need:
                # Update the best result if the current window is smaller.
                if r - l + 1 < resLen:
                    res = [l, r+1]
                    resLen = r - l + 1
                
                # Then shrink from the left
                window[s[l]] -= 1
                # the first removal of valid item leads window to break to look for next valid
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        # since r never reaches n, include n-1 as part of the final window
        return s[l:r] if resLen != float('inf') else ""