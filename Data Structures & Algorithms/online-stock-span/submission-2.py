class StockSpanner:

    def __init__(self):
        # create a stack
        self.stack = []
        

    def next(self, price: int) -> int:
        # count is default 1
        max_count = 1
        count = 1
        # keep a copy of stack as temp
        tmp = self.stack.copy()
        # while temp, check if last element is smaller than price to increase count by 1 and pop
        while tmp:
            if tmp[-1] <= price:
                count += 1
                tmp.pop()
            else:
                # update max_count
                max_count = max(max_count, count)
                # reset count for next iter
                count = 1
                break
        max_count = max(max_count, count)
        # append price to stack
        self.stack.append(price)
        # return count
        return max_count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)