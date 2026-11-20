# Count Pairs with Sum
# Solved
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

class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        left=0
        right=len(arr)-1
        count=0
        while left<right:
            total =arr[left]+arr[right]
            
            if total <target:
                left+=1
                
            elif total > target:
                right-=1
                
            else:
                left_value=arr[left]
                right_value=arr[right]
                
                if left_value == right_value:#This condition handles a special case: when the left and right pointers point to the same value, we need to count all possible pairs formed by that value.
                    n = right - left + 1
                    count += (n * (n - 1)) // 2
                    break
                
                left_count=0
                right_count=0
                
                while left<=right and arr[left]==left_value:
                    left_count+=1
                    left+=1
                while left<=right and arr[right]==right_value:
                    right_count+=1
                    right-=1
                    
                count+=left_count * right_count
                
        return count
        
        
        # Yes! You are absolutely right. You've understood the logic correctly. Let me clarify one small detail.

        # Inside the else condition, we count the occurrences of the matching values from both ends of the array.

        # 1. Left while loop: Starts from the current left pointer and moves towards the right, counting how many times left_value is repeated. Every occurrence increases left_count by 1, and left moves forward.

        # 2. Right while loop: Starts from the current right pointer and moves towards the left, counting how many times right_value is repeated. Every occurrence increases right_count by 1, and right moves backward.

        # 3. Finally: We multiply left_count * right_count to calculate all possible pairs between those two groups of repeated values.

        # One important point: Both loops use the same left and right pointers. They don't create new pointers; they continue moving the existing pointers to skip the duplicates already counted.

        # So your understanding is correct! Just remember that when left_value == right_value, we need a separate calculation using combinations rather than multiplying the two counts.
                