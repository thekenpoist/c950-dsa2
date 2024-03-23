class ChainedHashTable:
    
    def __init__(self, initial_cap=40):
        self.table = []
        for i in range(initial_cap):
            self.table.append([])

    def insert(self,key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_val in bucket_list:
            if key_val[0] == key:
                key_val[1] = item
                return True
            
            key_value = [key, item]
            bucket_list.append(key_value)
            return True
        
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_val in bucket_list:
            if key_val[0] == key:
                return key_val[1]
        
        return None
    
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_val in bucket_list:
            if key_val[0] == key:
                bucket_list.remove([key_val[0], key_val[1]])



