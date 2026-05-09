import heapq

# Create Empty Heap
heap = []

# Insert Elements
elements = [40, 10, 30, 50, 20]

print("Insertion Process:")

for item in elements:
    heapq.heappush(heap, item)
    print(f"Inserted {item} -> Heap: {heap}")

# Peek Minimum Element
print("\nTop Priority Element (Min):", heap[0])

# Extract Elements
print("\nExtraction Order:")

while heap:
    minimum = heapq.heappop(heap)
    print(f"Extracted {minimum} -> Remaining Heap: {heap}")