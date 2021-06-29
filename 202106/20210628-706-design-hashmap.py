class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.mod = 17
        self.data = [[] for i in range(self.mod)]

    def resize(self):
      new_mod = self.mod * 2 - 1
      new_data = [[] for i in range(new_mod)]

      for sub in self.data:
        for (key, val) in sub:
          new_data[key % new_mod].append((key, val))

      self.mod = new_mod
      self.data = new_data

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        k = key % self.mod
        sub = self.data[k]

        for (_key, _val) in sub:
          if key == _key:
            self.size -= 1
            sub.remove((_key, _val))
            break

        sub.append((key, value))
        self.size += 1

        if self.size >= self.mod // 2:
          self.resize()

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k = key % self.mod

        for (_key, _val) in self.data[k]:
          if key == _key:
            return _val

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        k = key % self.mod
        sub = self.data[k]

        for (_key, _val) in sub:
          if key == _key:
            sub.remove((_key, _val))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
