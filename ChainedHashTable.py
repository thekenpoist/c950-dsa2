# This module was created by Steve Hull, WGU ID# 011096053 and is code learned from  a combination of
# the zyBooks and Dr. Cemal Tepe's C950 - Data Structures and Algorithms II Webinar-1 "Let's Go Hashing".
# The ChainedHashTable module contains the necessary code to create a chained hash table that stores 
# data based upon a key/value pair. Comments in the code provide information about the program flow

class ChainedHashTable:

    def __init__(self, init_cap=40): # Set the capacity of the hash table to 40. Note: This number can be adjusted if needed
        self.table = [] # Initialize the table with an empty bucket
        for i in range(init_cap):
            self.table.append([])

    # Insert or update an item into the hash table based upon it's keys hash value
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # If the key is already in the bucket then update it
        for key_val in bucket_list:
            if key_val[0] == key:
                key_val[1] = item
                return True

        # If the key is not in the bucket, insert the item at the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search for an item based upon it's key. If a matching key is found
    # return that item. If it is not found, return None
    def search(self, key):
        # Start by getting the bucket where this key should be located
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Then search in the bucket list for the key and return that item if found
        for key_val in bucket_list:
            if key_val[0] == key:
                return key_val[1]

        return None

    # Remove an item that has a matching key
    def remove(self, key):
        # Start by getting the bucket where this key should be located
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Then remove the item from the bucket list if it is found
        for key_val in bucket_list:
            if key_val[0] == key:
                bucket_list.remove([key_val[0], key_val[1]])
