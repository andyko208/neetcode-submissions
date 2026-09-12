class MyHashSet:

    def __init__(self):
        self.hashset = [0] * 1000001

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        if self.hashset[key]:
            self.hashset[key] = 0

    def contains(self, key: int) -> bool:
        return bool(self.hashset[key])
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)