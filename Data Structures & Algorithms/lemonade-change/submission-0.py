class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # change options are 5, 10(10, 5+5), 15(10+5, 5+5+5)
        # keep a hashmap of counter
        counter = defaultdict(int)
        # iterate b in bills
        for b in bills:
            # change = b - 5
            change = b - 5
            # if change == 15, return False if counter[10] < 1 and counter[5] < 1
            if change == 15:
                if counter[10] > 0 and counter[5] > 0:
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] > 2:
                    counter[5] -= 3
                else:
                    return False
            # if change == 10, return False if counter[10] < 1 and counter[5] < 2
            elif change == 10:
                if counter[10] > 0:
                    counter[10] -= 1
                elif counter[5] > 1:
                    counter[5] -= 2
                else:
                    return False
            # if change == 5, return False if counter[5] < 1
            elif change == 5:
                if counter[5] > 0:
                    counter[5] -= 1
                else:
                    return False
            counter[b] += 1
        # return True
        return True