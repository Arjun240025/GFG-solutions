# Given an integer array arr[], return the sum of all elements of arr.

# Examples:

# Input: arr[] = [1, 2, 3, 4]
# Output: 10
# Explanation: 1 + 2 + 3 + 4 = 10.
# Input: arr[] = [1, 3, 3]
# Output: 7
# Explanation: 1 + 3 + 3 = 7.


class Solution:
    def arraySum(self, arr):
        sum = 0
        n = len(arr)

        for i in range(n):
            sum += arr[i]  # Add the array element

        return sum