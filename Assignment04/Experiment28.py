# Simple Bloom Filter Demo

size = 10

# Bit Array
bit_array = [0] * size


# Hash Functions
def hash1(item):
    return len(item) % size


def hash2(item):
    return sum(ord(c) for c in item) % size


# Insert Function
def insert(item):

    index1 = hash1(item)

    index2 = hash2(item)

    bit_array[index1] = 1
    bit_array[index2] = 1

    print(f"Inserted '{item}'")


# Search Function
def search(item):

    index1 = hash1(item)

    index2 = hash2(item)

    if bit_array[index1] == 1 and bit_array[index2] == 1:
        return "Possibly Present"

    return "Definitely Not Present"


# Insert Items
insert("cat")
insert("dog")
insert("apple")

# Display Bit Array
print("\nBit Array:")
print(bit_array)

# Queries
print("\nSearch Results:")

print("cat ->", search("cat"))
print("dog ->", search("dog"))
print("car ->", search("car"))
print("banana ->", search("banana"))