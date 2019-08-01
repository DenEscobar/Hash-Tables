

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        
        pass


# '''
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

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = LinkedPair(key, value)
    stored_pair = hash_table.storage[index]
    if hash_table.storage[index] is not None:
        if pair.key != stored_pair.key:
            stored_pair.next = pair

     
    else: 
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
    pass


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    if len(hash_table.storage) < hash_table.capacity * .3:
        hash_table.capacity = hash_table.capacity + ( hash_table.capacity * .5) 
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
