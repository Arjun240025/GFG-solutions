# Most Frequent of Two
# Solved
# Difficulty: BasicAccuracy: 44.36%Submissions: 134K+Points: 1
# Given an array arr[] and two elements x and y, return the element that occurs more frequently. If both elements have the same frequency, return the smaller one.

# Examples:

# Input: arr[] = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5], x = 4, y = 5
# Output: 4
# Explanation: frequency of 4 is 4.frequency of 5 is 1.Since 4>1 so return 4
# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], x = 1, y = 7
# Output: 1
# Explanation: frequency of 1 is 1.frequency of 7 is 1.Since 1 < 7, return 1.

class Solution:
    def moreFrequent(self, arr, x, y):
        count_x = 0  # Counts occurrences of x
        count_y = 0  # Counts occurrences of y

        for i in range(len(arr)):  # Visits every element
            if arr[i] == x:
                count_x += 1  # Increases count of x
            if arr[i] == y:
                count_y += 1  # Increases count of y

        if count_x > count_y:
            return x  # x occurs more frequently
        elif count_x < count_y:
            return y  # y occurs more frequently
        else:
            return min(x, y)  # Returns the smaller element if tied
        

#         Understanding in 5 Points
# 1. Initialize counters: count_x and count_y start at 0 to store how many times x and y appear.
# 2. Traverse the array: The for loop checks every element using arr[i].
# 3. Count occurrences: If arr[i] == x, we increase count_x. If arr[i] == y, we increase count_y.
# 4. Compare frequencies: If count_x > count_y, return x. If count_x < count_y, return y. Your original code returned the opposite element in these two cases.
# 5. Handle a tie: If both elements occur equally often, min(x, y) returns the smaller value.
# Remember this logic