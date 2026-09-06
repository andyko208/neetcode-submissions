class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # iterate through num and get 3 elements to store in the hashset as an int if all elements are the same
        # Time: O(N)
        n = len(num)
        max_substr = -1
        # Time: O(N)
        for i in range(n-2):
            if num[i] == num[i+1] == num[i+2]:
                # optimize by keeping the max here
                max_substr = max(max_substr, int(num[i:i+3]))
        # if max(hashset) is 0, return "000", if hashset if empty, return ""
        # print(substrs)
        if max_substr == 0:
            return "000"
        elif max_substr == -1:
            return ""
        return str(max_substr)
        