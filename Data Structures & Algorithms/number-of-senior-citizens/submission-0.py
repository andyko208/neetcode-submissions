class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Brute force
        count = 0
        # iterate through details and get the characters at details[i][11:13]
        for i in range(len(details)):
            # turn it to an int and increment count if > 60
            if int(details[i][11:13]) > 60:
                count += 1
        return count