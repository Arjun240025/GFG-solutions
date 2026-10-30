# Kadane's Algorithm
# Solved
# Difficulty: MediumAccuracy: 36.28%Submissions: 1.3MPoints: 4Average Time: 20m
# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.
# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

class Solution:
    def maxSubarraySum(self, arr):
        curr_sum = arr[0]  # Initialize current sum with the first element
        max_sum = arr[0]  # Initialize maximum sum with the first element

        # Loop from the second element to the last element
        for i in range(1, len(arr)):

            # Choose the current element alone or add it to the previous sum
            curr_sum = max(arr[i], curr_sum + arr[i])

            # Compare the maximum sum with the current sum and update if needed
            max_sum = max(max_sum, curr_sum)

        return max_sum  # Return the maximum subarray sum

#     Your explanation in 5 points
# 1. Initialization: curr_sum and max_sum are initialized with the first element of the array.
# 2. Loop: The loop starts at index 1 (the second element) and continues to the last element.
# 3. Calculate current sum: curr_sum = max(arr[i], curr_sum + arr[i]) chooses between starting a new subarray with the current element and extending the previous subarray.
# 4. Update maximum: max_sum = max(max_sum, curr_sum) compares the previous maximum with the current sum. If curr_sum is larger, max_sum is updated.
# 5. Return: After checking all elements, return max_sum returns the largest subarray sum.
# Small correction to your example: If the first element is 0 and the second is 1, then curr_sum = max(1, 0 + 1) = 1. We compare max_sum with curr_sum, so max_sum becomes 1.

