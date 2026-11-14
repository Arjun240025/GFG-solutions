# Zero Sum Subarray
# Solved
# Difficulty: MediumAccuracy: 39.79%Submissions: 332K+Points: 4Average Time: 20m
# Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. Return true/false depending upon whether there is a subarray present with 0-sum or not. 

# Examples:

# Input: arr[] = [4, 2, -3, 1, 6]
# Output: true
# Explanation: 2, -3, 1 is the subarray with a sum of 0.
# Input: arr = [4, 2, 0, 1, 6]
# Output: true
# Explanation: 0 is one of the elements in the array so there exist a subarray with sum 0.
# Input: arr = [1, 2, -1]
# Output: false

class Solution:
    def subArrayExists(self, arr):
        seen=set()
        curr_sum=0
        for i in range(len(arr)):
            curr_sum+=arr[i]
            
            if curr_sum==0:
                return True
            if curr_sum in seen:#If the same running sum appears twice, the elements between those two positions must have a sum of zero.
                return True
            seen.add(curr_sum)
        return False