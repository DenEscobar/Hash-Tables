

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        #self.count = 0
        self.storage = [None] * capacity
        pass


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + ord(i)
    return hash % max
    pass


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    stored_pair = hash_table.storage[index]
    if hash_table.storage[index] is not None:
        if pair.key != stored_pair.key:
            print(f"Warning: Index at {str(index)} is currently ({hash_table.storage[index]})). It will be overwritten")

    hash_table.storage[index] = pair
    pass


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        print(f'No item matching {key} exists')
    elif hash_table.storage[index].key == key:
        hash_table.storage[index] = None
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value

    return None
    pass


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
