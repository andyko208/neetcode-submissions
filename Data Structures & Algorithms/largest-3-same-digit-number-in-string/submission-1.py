class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # iterate through num and get 3 elements to store in the hashset as an int if all elements are the same
        substrs = set()
        n = len(num)
        for i in range(n-2):
            if num[i] == num[i+1] == num[i+2]:
                substrs.add(num[i:i+3])
        # if max(hashset) is 0, return "000", if hashset if empty, return ""
        # print(substrs)
        if substrs:
            max_substr = max(substrs)
            # print(max_substr)
            if max_substr == 0:
                return "000"
            else:
                return max_substr
        return ""
        