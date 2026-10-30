# Two Sum - Pair with Given Sum
# Solved
# Difficulty: EasyAccuracy: 30.61%Submissions: 623K+Points: 2Average Time: 20m
# Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

# Examples:

# Input: arr[] = [0, -1, 2, -3, 1], target = -2
# Output: true
# Explanation: arr[3] + arr[4] = -3 + 1 = -2
# Input: arr[] = [1, -2, 1, 0, 5], target = 0
# Output: false
# Explanation: None of the pair makes a sum of 0
# Input: arr[] = [11], target = 11
# Output: false
# Explanation: No pair is possible as only one element is present in arr[]

class Solution:
    def twoSum(self, arr, target):
        seen = set()  # Stores the elements we have already visited

        for i in range(len(arr)):
            need = target - arr[i]  # Find the value needed to get the target

            # If the need value is already in seen, the current element
            # and the previously stored element add up to the target.
            # So, we stop the function and return True.
            if need in seen:
                return True

            # If the need value is not in seen, add the current element
            # to seen and continue to the next element.
            seen.add(arr[i])

        return False  # No pair found

#     Yes! ✅ Exactly right.

# If the new need value is already present in the seen set, the execution stops immediately because of return True.