class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_list = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.my_list[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.my_list[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.my_list[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)