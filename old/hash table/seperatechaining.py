HashTable = [[] for _ in range (10)]

def display(hashTable):
    for i in range(len(hashTable)):
        print(i, end = " ")

        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")

        print()

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

if __name__ == "__main__":
    insert(HashTable, 10, 'Allahabad')
    insert(HashTable, 25, 'Mumbai')
    insert(HashTable, 20, 'Mathura')
    insert(HashTable, 9, 'Delhi')
    insert(HashTable, 21, 'Punjab')
    insert(HashTable, 21, 'Noida')
    
    display(HashTable)