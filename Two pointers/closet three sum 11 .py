# Closest Three Sum
# Solved
# Difficulty: MediumAccuracy: 17.65%Submissions: 93K+Points: 4Average Time: 30m
# Given an array, arr[] of integers, and another number target, find three integers in the array such that their sum is closest to the target. Return the sum of the three integers.

# Note: If there are multiple solutions, return the maximum one.

# Examples :

# Input: arr[] = [-1, 2, 2, 4], target = 4
# Output: 5
# Explanation: All possible triplets
# [-1, 2, 2], sum = (-1) + 2 + 2 = 3
# [-1, 2, 4], sum = (-1) + 2 + 4 = 5
# [-1, 2, 4], sum = (-1) + 2 + 4 = 5
# [2, 2, 4], sum = 2 + 2 + 4 = 8
# Triplet [-1, 2, 2], [-1, 2, 4] and [-1, 2, 4] have sum closest to target, so return the maximum one, that is 5.
# Input: arr[] = [1, 10, 4, 5], target = 10
# Output: 10
# Explanation: All possible triplets
# [1, 10, 4], sum = (1 + 10 + 4) = 15
# [1, 10, 5], sum = (1 + 10 + 5) = 16
# [1, 4, 5], sum = (1 + 4 + 5) = 10
# [10, 4, 5], sum = (10 + 4 + 5) = 19 
# Triplet [1, 4, 5] has sum = 10 which is closest to target.

class Solution:
    def closest3Sum(self, arr, target):
        # code here
        arr.sort()
        closet=arr[0]+arr[1]+arr[2]
        for i in range(len(arr)-2):
            left=i+1
            right=len(arr)-1
            
            while left<right:
                total=arr[i]+arr[left]+arr[right]
                
                if abs(total-target)<abs(closet-target):
                    closet=total
                elif abs(total-target)==abs(closet-target):
                    closet=max(closet,total)
                
                if total < target:
                    left+=1
                elif total > target:
                    right-=1
                else:
                    return total
        return closet