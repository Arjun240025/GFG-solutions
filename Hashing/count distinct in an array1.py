# Count Distinct in Array
# Solved
# Difficulty: BasicAccuracy: 73.07%Submissions: 34K+Points: 1
# Given an integer array arr[], return the count of all the distinct elements in an array

# Examples:

# Input: arr[] = [2, 2, 3, 2]
# Output: 2
# Explanation: Distinct elements are {2, 3}
# Input: arr[] = [12, 1, 14, 3, 16]
# Output: 5
# Explanation: Distinct elements are {12, 1, 14, 3, 16}
# Input: arr[] = [1, 1, 1, 1]
# Output: 1
# Explanation: Only one distinct element {1}  

class Solution:
    def countDistinct(self, arr: list[int]) -> int:
        # code here
        a = set(arr)#converts the list arr into a set, which automatically removes any duplicate elements. The resulting set a contains only the distinct elements from arr.
        return len(a)