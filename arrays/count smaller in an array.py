# Count Smaller in Array
# Solved
# Difficulty: BasicAccuracy: 54.54%Submissions: 160K+Points: 1Average Time: 20m
# Given an unsorted array arr[]. Find the count of elements less than or equal to the given element x.

# Examples:

# Input: x = 9, arr[] = [10, 1, 2, 8, 4, 5] 
# Output: 5
# Explanation: The 5 elements are 1, 2, 8, 4 and 5.
# Input: x = 2, arr[] = [1, 2, 2, 5, 7, 2, 9] 
# Output: 4 
# Explanation: The 4 elements are 1, 2, 2 and 2.

class Solution:
    def countOfElements(self, x, arr):
        n=len(arr)
        count=0
        for i in range(n):
            if arr[i]<=x:
                count+=1
        return count
        

# Understanding in 5 Points
# 1. Initialize count = 0: We declare a variable to count how many elements are less than or equal to x. Initially, it is 0 because we haven't checked any elements.
# 2. Loop through the array: for i in range(len(arr)) visits every index, and arr[i] gives the current element.
# 3. Check the condition: if arr[i] <= x checks whether the current element is less than or equal to x.
# 4. Increase the count: If the condition is true, count += 1 increases the count by one. Otherwise, the count remains unchanged.
# 5. Return the result: After checking all elements, return count gives the total number of elements satisfying the condition.  