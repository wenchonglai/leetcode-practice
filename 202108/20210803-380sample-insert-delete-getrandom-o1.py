class RandomizedSet:
    # Hash+Array+Math.random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.h = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.h:
          return False
        
        self.h[val] = len(self.arr)
        self.arr.append(val)
        
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.h:
          return False
        
        i = self.h[val]
        last = len(self.arr) - 1
        
        del self.h[val]
        
        if i != last:
          self.arr[i] = self.arr[last]
          self.h[self.arr[i]] = i
          
        self.arr.pop()
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[randint(0, len(self.arr) - 1)]