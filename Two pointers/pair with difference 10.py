# Pair With Difference
# Solved
# Difficulty: EasyAccuracy: 27.25%Submissions: 309K+Points: 2Average Time: 15m
# Given an array, arr[] and an integer x, return true if there exists a pair of elements in the array whose absolute difference is x, otherwise, return false.

# Examples:

# Input: arr[] = [5, 20, 3, 2, 5, 80], x = 78
# Output: true
# Explanation: Pair (2, 80) have an absolute difference of 78.
# Input: arr[] = [90, 70, 20, 80, 50], x = 45
# Output: false
# Explanation: There is no pair with absolute difference of 45.

class Solution:
    def findPair(self, arr: list[int], x: int) -> int:
        arr.sort()

        left = 0
        right = 1

        while right < len(arr):#This ensures that right stays within the valid array indexes.
            if left == right:#This part is used to prevent both pointers from pointing to the same array element.
                right += 1
                continue

            total = arr[right] - arr[left]

            if total == x:
                return True

            elif total < x:
                right += 1

            else:
                left += 1

        return False