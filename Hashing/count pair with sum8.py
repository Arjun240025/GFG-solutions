# Count Pairs with Sum
# Difficulty: MediumAccuracy: 50.11%Submissions: 71K+Points: 4Average Time: 15m
# You are given an array arr[] and an integer target. You have to count all pairs in the array such that their sum is equal to the given target.

# Examples:

# Input: arr[] = [1, 5, 7, -1, 5], target = 6 
# Output: 3
# Explanation: Pairs with sum 6 are (1, 5), (7, -1) and (1, 5). 
# Input: arr[] = [1, 1, 1, 1], target = 2 
# Output: 6
# Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).
# Input: arr[] = [10, 12, 10, 15, -1], target = 125
# Output: 0
# Explanation: There is no pair with sum = target


#1(not optimal)(brute force approach)
class Solution:
    def countPairs(self, arr, target):
        #code here
        count=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==target:
                    count+=1
        return count

#2(optimal)(using hashing)
class Solution:
    def countPairs(self, arr, target):
        freq = {}  # Stores elements and their frequencies
        count = 0

        for i in arr:
            need = target - i  # Find the element needed to make target

            # Check whether the required element is already in dictionary
            if need in freq:#same as two sum leetcode-19 if the need is already  present in the freq then it is a pair and is counted
                count += freq[need]

            # Store the current element and increase its frequency
            freq[i] = freq.get(i, 0) + 1

        return count