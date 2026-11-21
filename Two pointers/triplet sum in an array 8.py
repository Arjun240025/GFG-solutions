# Triplet Sum in Array
# Solved
# Difficulty: MediumAccuracy: 35.0%Submissions: 397K+Points: 4Average Time: 15m
# Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

# Return true if such a triplet exists, otherwise, return false.

# Examples: 

# Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
# Output: true 
# Explanation: The triplet {1, 4, 8} sums up to 13.
# Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10
# Output: true 
# Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10. 
# Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24
# Output: false 
# Explanation: No triplet in the array sums to 24.

class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        arr.sort()
        for i in range(len(arr)-2):#first element to add
            left=i+1#second element since the first element is i
            right=len(arr)-1#last element or the third element
            
            while left<right:
                total = arr[i]+arr[left]+arr[right]
                
                if total == target:
                    return True
                elif total <target:
                    left+=1
                else:
                    right-=1
        return False
        
        # 3. How do you identify whether sorting is needed?
        # Remember these rules:
        # Rule 1: Two pointers based on sum

        # If you need to move left or right depending on whether the sum is greater or smaller than the target, sorting is generally needed.

        # Rule 2: Hashing

        # If you're using a dictionary or set to find elements, sorting is generally unnecessary.

        # Rule 3: Already sorted input

        # If the problem says the array is sorted, don't sort it again.
        
        
#         1. Problems where sorting is useful or necessary
# 		Problem	Should we sort?	Reason
# 		Two Sum (Two Pointers)	Yes	Move pointers based on sum
# 		Two Sum II (Sorted Array)	No	Array is already sorted
# 		Triplet Sum	Yes	Fix one element and find the other two
# 		4Sum	Yes	Use sorting and two pointers
# 		Pair with Given Sum	Yes, for two pointers	Compare smallest and largest
# 		3Sum	Yes	Find triplets efficiently
# 		Merge Intervals	Yes	Arrange intervals by starting point