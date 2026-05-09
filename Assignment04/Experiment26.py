# Hash Table using Separate Chaining

class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash Function
    def hash_function(self, key):
        return key % self.size

    # Insert Function
    def insert(self, key, value):

        index = self.hash_function(key)

        self.table[index].append((key, value))

    # Get/Search Function
    def get(self, key):

        index = self.hash_function(key)

        for k, v in self.table[index]:

            if k == key:
                return v

        return "Key Not Found"

    # Delete Function
    def delete(self, key):

        index = self.hash_function(key)

        bucket = self.table[index]

        for pair in bucket:

            if pair[0] == key:

                bucket.remove(pair)

                return "Deleted Successfully"

        return "Key Not Found"

    # Display Hash Table
    def display(self):

        print("\nHash Table:")

        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# Main Program
ht = HashTable(5)

# Insert Key-Value Pairs
ht.insert(10, "Apple")
ht.insert(15, "Banana")
ht.insert(20, "Orange")
ht.insert(7, "Mango")
ht.insert(12, "Grapes")

# Display Table
ht.display()

# Get Value
print("\nGet Key 15:", ht.get(15))

# Delete Key
print("\nDelete Key 20:", ht.delete(20))

# Display After Deletion
ht.display()