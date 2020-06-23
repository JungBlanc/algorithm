hash_table = [0 for i in range(10)]

data = ['Andy', 'Dave', 'Trump', 'Anthor']

def hash_function(key):
    return key % 10

def store_hash(data, value) :
    key = ord(data)
    hash_adress = hash_function(data)
    hash_table[hash_adress] = value



