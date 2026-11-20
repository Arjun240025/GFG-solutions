# Intersection of Two Sorted Arrays
# Solved
# Difficulty: EasyAccuracy: 42.53%Submissions: 119K+Points: 2
# Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.
# Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.
# Note: If there is no intersection then return an empty array.

# Examples:

# Input: arr1[] = [1, 2, 3, 4], arr2[] = [2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are only common elements in both the arrays.
# Input: arr1[] = [1, 2, 2, 3, 4], arr2[] = [2, 2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are the only common elements.
# Input: arr1[] = [1, 2], arr2[] = [3, 4]
# Output: []
# Explanation: No common elements.

class Solution:
    def intersection(self, arr1, arr2):
        i = 0
        j = 0
        res = []

        # Continue until either array has been completely traversed
        while i < len(arr1) and j < len(arr2):

            # If arr1 element is smaller, move i forward
            if arr1[i] < arr2[j]:
                i += 1

            # If arr2 element is smaller, move j forward
            elif arr1[i] > arr2[j]:
                j += 1

            # If both elements are equal, it is a common element
            else:
                # Add only if it is not already present in res
                if not res or res[-1] != arr1[i]:
                    res.append(arr1[i])#in inersection only the  equal elements in ythe both the array are appended!!!

                # Move both pointers because both elements matched
                i += 1
                j += 1

        return res