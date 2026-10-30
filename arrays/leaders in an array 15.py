# Array Leaders
# Solved
# Difficulty: EasyAccuracy: 29.94%Submissions: 1.1MPoints: 2Average Time: 15m
# You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

# Examples:

# Input: arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
# Input: arr = [10, 4, 2, 4, 1]
# Output: [10, 4, 4, 1]
# Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side
# Input: arr = [5, 10, 20, 40]
# Output: [40]
# Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
# Input: arr = [30, 10, 10, 5]
# Output: [30, 10, 10, 5]
# Explanation: When an array is sorted in non-increasing order, all elements are leaders.



class Solution:
    def leaders(self, arr):
        res = []  # Stores all leader elements

        leader = arr[-1]  # Last element is always a leader
        res.append(leader)  # Add the last element to the result

        # Start from the second-last index and move towards index 0
        for i in range(len(arr) - 2, -1, -1):

            # Check if the current element is >= the largest element on its right
            if arr[i] >= leader:
                res.append(arr[i])  # Add the current element as a leader
                leader = arr[i]  # Update the largest element found so far

        res.reverse()  # Reverse to restore the original array order
        return res  # Return the list of leaders



#     Understanding in 5 Points
# 1. Initialize res and leader: We create an empty list res to store the leaders. We initialize leader = arr[-1] because the rightmost element is always a leader, and append it to res.
# 2. Understand the loop: range(len(arr) - 2, -1, -1) starts from the second-last index and moves backwards, one index at a time, until index 0. We use -1 as the stopping boundary because Python excludes the stop value, allowing index 0 to be included.
# 3. Check the condition: if arr[i] >= leader checks whether the current element is greater than or equal to the largest element found on its right.
# 4. Add and update: If the condition is true, we append arr[i] to res and update leader = arr[i]. Otherwise, we skip the element because a greater element exists on its right.
# 5. Reverse and return: Since we traverse from right to left, the leaders are stored in reverse order. res.reverse() restores their original order, and return res gives the final answer.