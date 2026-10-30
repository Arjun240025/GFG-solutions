# Sort 0s, 1s and 2s
# Solved
# Difficulty: MediumAccuracy: 50.58%Submissions: 892K+Points: 4Average Time: 10m
# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order. 

# Examples:

# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.
# Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.

#1
class Solution:
    def sort012(self, arr):
        # code here
        arr.sort()
        return arr

#2
class Solution:
    def sort012(self, arr):
        count_0 = arr.count(0)  # Count the number of zeros
        count_1 = arr.count(1)  # Count the number of ones
        count_2 = arr.count(2)  # Count the number of twos

        # Replace the array elements in sorted order
        arr[:count_0] = [0] * count_0
        arr[count_0:count_0 + count_1] = [1] * count_1
        arr[count_0 + count_1:] = [2] * count_2

        return arr