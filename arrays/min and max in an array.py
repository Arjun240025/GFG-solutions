# Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

# Examples:

# Input: arr[] = [1, 4, 3, 5, 8, 6]
# Output: [1, 8]
# Explanation: minimum and maximum elements of array are 1 and 8.
# Input: arr[] = [12, 3, 15, 7, 9]
# Output: [3, 15]
# Explanation: minimum and maximum element of array are 3 and 15.

class Solution:
    def getMinMax(self, arr):
        # code here
        n=len(arr)
        x=arr[0]
        y=arr[0]
        for i in range(n):
            if arr[i]<x:
                x=arr[i]
            if arr[i]>y:
                y=arr[i]
        return [x,y]