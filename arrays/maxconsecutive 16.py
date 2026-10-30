# Max Same Consecutive
# Solved
# Difficulty: EasyAccuracy: 49.84%Submissions: 57K+Points: 2
# Given an array arr[] consisting of only 0’s and 1’s, return count of the maximum number of consecutive 1’s or 0’s present in the array. 

# Examples:

# Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
# Output: 4
# Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6.
# Input: arr[] = [0, 0, 1, 0, 1, 0]
# Output: 2
# Explanation: The maximum number of consecutive 0’s in the array is 2 from index 0-1.
# Input: arr[] = [0, 0, 0, 0]
# Output: 4
# Explanation: The maximum number of consecutive 0’s in the array is 4.

class Solution:
    def maxConsecBits(self, arr):
        count_0 = 0  # Counts consecutive zeros
        count_1 = 0  # Counts consecutive ones
        max_count = 0  # Stores the maximum consecutive count

        for i in range(len(arr)):  # Checks every array element
            if arr[i] == 0:
                count_0 += 1  # Increments zero count
                count_1 = 0  # Resets one count

            else:
                count_1 += 1  # Increments one count
                count_0 = 0  # Resets zero count

            # Updates the maximum consecutive count found so far
            max_count = max(max_count, count_0, count_1)

        return max_count  # Returns the maximum consecutive count

#     Understanding in 5 Points
# 1. Initialize: count_0 counts consecutive zeros, count_1 counts consecutive ones, and max_count stores the longest sequence found so far.
# 2. Traverse: The for loop checks every element using arr[i].
# 3. Count consecutive bits: If the element is 0, increment count_0 and reset count_1. Otherwise, increment count_1 and reset count_0.
# 4. Update the maximum: max() compares the previous maximum with the current zero and one counts. If a longer sequence appears, max_count is updated.
# 5. Return: After checking all elements, return max_count gives the maximum number of consecutive identical bits.
# Example: arr = [0, 1, 1, 1, 0] → Output: 3