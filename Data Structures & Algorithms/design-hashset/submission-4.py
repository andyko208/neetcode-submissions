class MyHashSet:

    def __init__(self):
        self.hashset = defaultdict(int)

    def add(self, key: int) -> None:
        self.hashset[key] = 1

    def remove(self, key: int) -> None:
        self.hashset[key] -= 1

    def contains(self, key: int) -> bool:
        if self.hashset[key] > 0:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)