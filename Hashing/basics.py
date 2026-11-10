# 1. What is Hashing?
# Hashing is a technique used to store and retrieve data efficiently using a key.

# In Python, we mainly use two data structures:
# - Dictionary (dict) – Stores key-value pairs.
# - Set (set) – Stores unique elements.

arr = [1, 2, 2, 3, 3, 3, 4]

# Count the frequency of each element
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)