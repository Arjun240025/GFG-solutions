# Two Sum in Sorted Array
# Solved
# Difficulty: EasyAccuracy: 49.95%Submissions: 17K+Points: 2
# Given an array arr[] that is sorted in non-decreasing order, along with an integer target. Your task is to find positions of two elements with sum equal to target.

# If such a pair exists, return the positions (index + 1)  of the two elements in increasing order.   
# If no such pair exists, return [-1, -1].
# Note: If your answer is correct then the driver code will print "true" otherwise "false". Since there can be multiple answers, the driver code mainly checks whether the pair returned by your code is correct or not.

# Examples:

# Input: arr[] = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Explanation: Since arr[0] + arr[1] = 2 + 7 = 9 equals the target, return their 1-based indices : [1, 2]
# Input: arr[] = [1, 3, 4, 6, 8, 11], target = 10
# Output: [3, 4]
# Explanation: Since arr[2] + arr[3] = 4 + 6 = 10 equals the target, return their 1-based indices : [3, 4]

class Solution:
    def twoSum(self, arr, target):
        left=0
        right=len(arr)-1
        while left<right:
            total=arr[left]+arr[right]
            
            if total == target:
                return [left+1,right+1]
            elif total < target:
                left+=1
            else:
                right-=1
        return [-1,-1]