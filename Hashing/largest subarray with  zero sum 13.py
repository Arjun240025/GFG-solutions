# Largest Subarray with 0 Sum
# Solved
# Difficulty: MediumAccuracy: 41.84%Submissions: 493K+Points: 4Average Time: 20m
# Given an array arr[] containing both positive and negative integers, the task is to find the length of the longest subarray with a sum equals to 0.

# Note: A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.

# Examples:

# Input: arr[] = [15, -2, 2, -8, 1, 7, 10, 23]
# Output: 5
# Explanation: The longest subarray with sum equals to 0 is [-2, 2, -8, 1, 7].
# Input: arr[] = [2, 10, 4]
# Output: 0
# Explanation: There is no subarray with a sum of 0.
# Input: arr[] = [1, 0, -4, 3, 1, 0]
# Output: 5
# Explanation: The longest subarray with sum equals to 0 is [0, -4, 3, 1, 0]

class Solution:
    def maxLength(self, arr):
        # code here
        freq={0:-1}
        curr_sum=0
        max_len=0
        for i in range(len(arr)):
            curr_sum+=arr[i]
            
            if curr_sum in freq:
                length = i-freq[curr_sum]
                max_len=max(length,max_len)
            else:
                freq[curr_sum]=i
        return max_len
        
# 1. Why if curr_sum in freq?
# It checks whether the current prefix sum has already appeared before.

# If the same prefix sum appears twice, the elements between those two positions must have a sum of 0.
# 2. Why length = i - freq[curr_sum]?
# - i = current index.
# - freq[curr_sum] = first index where this prefix sum appeared.
# - Subtracting them gives the length of the zero-sum subarray.
# 3. Why max_len = max(max_len, length)?
# It compares:
# - max_len = longest length found so far.
# - length = newly found zero-sum subarray length.