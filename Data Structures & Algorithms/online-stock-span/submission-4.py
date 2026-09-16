class StockSpanner:

    def __init__(self):
        # create a stack
        self.stack = []
        

    def next(self, price: int) -> int:
        # monotonic stack approach Time O(N), Space: O(N)
        # while price is bigger than or eq to last item in the stack, update count to last item's count += current count and pop
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack[-1][1]
            self.stack.pop()
        # append price to the stack as (price, count)
        self.stack.append((price, count))
        # return count
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)