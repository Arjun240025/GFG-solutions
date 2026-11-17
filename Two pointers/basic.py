# 1. What is the Two Pointers Technique?
# Two Pointers is a technique where we use two variables to track positions in a data structure, usually an array or string.

arr = [1, 2, 3, 4, 5, 6]

left = 0
right = len(arr) - 1

while left < right:
    print(arr[left], arr[right])

    left += 1
    right -= 1