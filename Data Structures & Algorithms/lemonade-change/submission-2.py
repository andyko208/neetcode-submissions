class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # keep track of 5 and 10 bills, 20 bill is irrelevant
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five -= 1
                ten += 1
            elif ten > 0: # b == 20 is assumed
                ten -= 1
                five -= 1
            else:   # b == 20 and ten == 0, need to change with only fives
                five -= 3
            if five < 0:
                return False
        return True