# This module was created by Steve Hull, and is comprised of some code learned from 
# C950 - Data Structures and Algorithms II. The ChainedHashTable module contains the 
# necessary code to create a chained hash table that stores data based upon a key/value pair. 

class ChainedHashTable:

    def __init__(self, init_cap=40): 
        self.table = [] 
        for i in range(init_cap):
            self.table.append([])

    def insert(self, key, item):
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
