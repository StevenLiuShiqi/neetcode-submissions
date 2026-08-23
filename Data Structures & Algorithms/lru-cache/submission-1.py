class LRUCache:
    class Node:
        def __init__(self, val:int=0, key:int=0):
            self.prev = None
            self.next = None
            self.val = val
            self.key = key

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.full = False
        self.LRU = self.Node(0)
        self.MRU = self.Node(0)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU

    def putAtBack(self, n: Node):
        n.prev, n.next = self.MRU.prev, self.MRU
        self.MRU.prev.next = n
        self.MRU.prev = n

    def evict(self, n: Node):
        n.prev.next = n.next
        n.next.prev = n.prev
        

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            n = self.cache[key]
            self.evict(n)
            self.putAtBack(n)
            return n.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            n = self.Node(value, key)
            if self.full:
                self.cache.pop(self.LRU.next.key)
                self.evict(self.LRU.next)
            self.putAtBack(n)
            self.cache[key] = n
            if not self.full:
                self.capacity -= 1
                if self.capacity <= 0:
                    self.full = True
        else:
            n = self.cache[key]
            n.val = value
            self.evict(n)
            self.putAtBack(n)

        
