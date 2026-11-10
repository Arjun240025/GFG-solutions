# Two Arrays Permutation Check
# Solved
# Difficulty: EasyAccuracy: 42.18%Submissions: 463K+Points: 2Average Time: 30m
# Given two arrays a[] and b[] of equal size, the task is to find whether the given arrays are permutation of each other. Two arrays are said to be permutation if both contain the same set of elements, arrangements of elements may be different though.

# Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be permutation.

# Examples:

# Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
# Output: true
# Explanation: Both arrays contain the same elements and can be rearranged to [0, 1, 2, 4, 5]. Therefore, the output is true.
# Input: a[] = [1, 2, 5], b[] = [2, 4, 15]
# Output: false
# Explanation: a[] and b[] have only one common value, 2. All others elements are different so the arrays cannot be rearranged to become equal. Therefore, the output is false.

class Solution:
    def checkPermutation(self, a, b):
        # Both arrays must have the same number of elements
        if len(a) != len(b):
            return False

        freq = {}  # Stores each element and its frequency

        # First loop: Count how many times each element occurs in array a
        for i in a:
            # Get the current frequency; if the element is new, use 0.
            # Increase its frequency by 1.
            freq[i] = freq.get(i, 0) + 1

        # Second loop: Check elements in array b
        for i in b:

            # Check whether the current element exists in array a
            if i not in freq:
                return False

            # Reduce the frequency because we have matched this element
            freq[i] -= 1

            # If frequency becomes negative, array b contains this element
            # more times than array a. So, they are not permutations.
            if freq[i] < 0:
                return False

        # If all elements are matched with the correct frequencies,
        # both arrays are permutations of each other.
        return True