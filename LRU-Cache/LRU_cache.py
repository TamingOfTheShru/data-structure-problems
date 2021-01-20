# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

#approach 1, using ordered_dict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# approach 2, using deque            
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.q = deque()
        self.timestamp = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            item = self.cache[key]
            item[1] = self.timestamp
            print(item)
            self.q.append((self.timestamp, key))
            self.timestamp+=1
            return item[0]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            while True:
                t, k = self.q.popleft()
                print(t,k)
                if self.cache[k][1] == t:
                    break
                self.cache.pop(k)
        self.cache[key] = [value, self.timestamp]
        self.q.append((self.timestamp, key))
        
        self.timestamp+=1

#Your LRUCache object will be instantiated and called as such:
#obj = LRUCache(capacity)
#param_1 = obj.get(key)
#obj.put(key,value)

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
