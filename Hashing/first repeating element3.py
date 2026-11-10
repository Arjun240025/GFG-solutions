# First Repeating Element
# Solved
# Difficulty: EasyAccuracy: 32.57%Submissions: 347K+Points: 2Average Time: 15m
# Given an array arr[], find the first repeating element position. The element should occur more than once and the position (from left) of its first occurrence should be the smallest.

# Note: The position you return should be according to 1-based indexing. 

# Examples:

# Input: arr[] = [1, 5, 3, 4, 3, 5, 6]
# Output: 2
# Explanation: 5 appears twice and its first appearance is at position 2 which is less than 3 whose first the occurring position is 3.
# Input: arr[] = [1, 2, 3, 4]
# Output: -1
# Explanation: All elements appear only once so answer is -1.

class Solution:
    def firstRepeated(self, arr):
        freq = {}  # Stores each element and how many times it occurs

        # First loop: Count the frequency of every element
        for i in arr:
            # Get the current frequency; if the element is new, start from 0.
            # Then increase its frequency by 1.
            freq[i] = freq.get(i, 0) + 1

        # Second loop: Check elements from left to right
        for i in range(len(arr)):
            # arr[i] gives the current element.
            # freq[arr[i]] gives how many times that element occurs.
            # If its frequency is greater than 1, it is a repeating element.
            if freq[arr[i]] > 1:#only check first repeating element and return

                # Return i + 1 because GFG asks for 1-based position.
                # return immediately stops the function because we found
                # the first repeating element from the left.
                return i + 1

        # If the loop finishes without finding any repeating element,
        # return -1 as required by the problem.
        return -1