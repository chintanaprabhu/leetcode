class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        ## linear hashing, we have a table with 1000 slots, each slot has 1000 grid
        self.table_size = 1000
        self.slot_size = 1000
        self.table = [ [] for _ in range(self.table_size) ]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.table_size
        slot_key = key // self.slot_size
        if 0 == len(self.table[hash_key]):
            # create slot on demand in run-time
            self.table[hash_key] = [ -1 for _ in range(self.slot_size)]
        # update key-value pair
        self.table[hash_key][slot_key] = value
        return
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.table_size
        slot_key = key // self.slot_size
        if len(self.table[hash_key]):
            # get corresponding value if given key exists in our table
            return self.table[hash_key][slot_key]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.table_size
        slot_key = key // self.slot_size
        if len(self.table[hash_key]): 
            # reset to -1 if given key exists in our table
            # otherwise, do nothing
            self.table[hash_key][slot_key] = -1  
        return
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
