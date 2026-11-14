# Subarrays with Sum K
# Solved
# Difficulty: MediumAccuracy: 49.74%Submissions: 156K+Points: 4
# Given an unsorted array arr[] of integers, find the number of subarrays whose sum exactly equal to a given number k.

# Examples:

# Input: arr[] = [10, 2, -2, -20, 10], k = -10
# Output: 3
# Explanation: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.
# Input: arr[] = [9, 4, 20, 3, 10, 5], k = 33
# Output: 2
# Explanation: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.
# Input: arr[] = [1, 3, 5], k = 0
# Output: 0
# Explanation: No subarray with 0 sum.

class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        freq={0:1}
        curr_sum=0
        count=0
        for i in range(len(arr)):
            curr_sum+=arr[i]
            
            need=curr_sum-k
            
            count+=freq.get(need,0)#if the current need already exists in the dict this method increases the value of count by 
        #Yes! Exactly. It uses the existing frequency (number of occurrences) of the need value in the dictionary
            freq[curr_sum]=freq.get(curr_sum,0)+1
        return count