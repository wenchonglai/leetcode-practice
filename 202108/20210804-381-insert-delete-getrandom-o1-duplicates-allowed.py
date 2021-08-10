class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        bol = False

        if val not in self.h:
          self.h[val] = []
          bol = True

        self.h[val].append(len(self.arr))
        self.arr.append(val)

        return bol

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.h:
          return False

        i = self.h[val].pop()
        lastIdx = len(self.arr) - 1
        lastVal = self.arr[-1]

        if i != lastIdx:
          self.h[lastVal].pop()
          arr = self.h[lastVal]

          idx = bisect.bisect_left(arr, i)
          self.h[lastVal] = arr[:idx] + [i] + arr[idx:]
          self.arr[i] = lastVal

        self.arr.pop()

        if not self.h[val]:
          del self.h[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
