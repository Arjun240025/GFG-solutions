# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        arr.sort()
        largest = arr[-1]

        for i in range(n - 2, -1, -1):#n-2 because we are starting from the second last element and going backwards to the first element,-1 because we want to include the first element in the loop,-1 because we want to decrement the index by 1 in each iteration
            if arr[i] != largest:
                return arr[i]

        return -1