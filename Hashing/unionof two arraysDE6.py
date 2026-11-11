# Union of Arrays with Duplicates
# Solved
# Difficulty: EasyAccuracy: 42.22%Submissions: 519K+Points: 2Average Time: 10m
# You are given two arrays a[] and b[], return the union of both the arrays in any order. 

# Elements of a[] and b[] are not necessarily distinct, but output should have only distinct elements.
# The returned union may have elements in any order, the driver code will print the result in sorted order only.
# Examples:

# Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
# Output: [1, 2, 3]
# Explanation: Union set of both the arrays will be 1, 2 and 3.
# Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
# Output: [1, 2, 3, 4, 5, 6]
# Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.
# Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
# Output: [1, 2]
# Explanation: Union set of both the arrays will be 1 and 2.

class Solution:
    def findUnion(self, a, b):
        c = set(a)  # Remove duplicates from array a
        d = set(b)  # Remove duplicates from array b

        # Combine both sets and remove common duplicates
        res = c | d

        return list(res)  # Convert the set into a list