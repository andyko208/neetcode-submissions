class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time: O(N), Memory: O(N)
        # If t is empty, return "".
        if t == "":
            return ""

        countT, window = Counter(t), Counter()
        # Build a frequency map countT for characters in t.
        # for c in t:
        #     countT[c] = 1 + countT.get(c, 0)
        # print(countT)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            # Add s[r] to window.
            c = s[r]
            window[c] += 1

            # If s[r] is in countT and its count in window matches countT, increment have.
            if window[c] == countT[c]:
                have += 1

            # window is valid
            while have == need:
                # Update the best result if the current window is smaller.
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # Then shrink from the left
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""