class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.arrSize = 4
        self.mod = self.arrSize + 1
        self.arr = [[] for i in range(self.mod)]

    def add(self, key: int) -> None:
        if not self.contains(key):
          self.arr[key % self.mod].append(key)
          self.size += 1

          if self.size >= self.arrSize // 2:
            self.rehash()

    def rehash(self, up=True):
      newSize = self.arrSize * 2 if up else self.arrSize // 2
      newMod = newSize + 1
      newArr = [[] for i in range(newMod)]

      for sub in self.arr:
        for num in sub:
          newKey = num % newMod
          newArr[newKey].append(num)

      self.arrSize = newSize
      self.mod = newMod
      self.arr = newArr

    def remove(self, key: int) -> None:
      if self.contains(key):
        self.arr[key % self.mod].remove(key)
        self.size -= 1

        if self.size <= self.arrSize // 4:
          self.rehash(False)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.mod
        return key in self.arr[idx]

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
