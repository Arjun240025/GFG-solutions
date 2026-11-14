# Count Distinct Elements in Every Window
# Difficulty: MediumAccuracy: 41.83%Submissions: 194K+Points: 4Average Time: 20m
# Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

# Examples:

# Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
# Output: [3, 4, 4, 3]
# Explanation:
# First window is [1, 2, 1, 3], count of distinct numbers is 3.
# Second window is [2, 1, 3, 4] count of distinct numbers is 4.
# Third window is [1, 3, 4, 2] count of distinct numbers is 4.
# Fourth window is [3, 4, 2, 3] count of distinct numbers is 3.
# Input: arr[] = [4, 1, 1], k = 2
# Output: [2, 1]
# Explanation:
# First window is [4, 1], count of distinct numbers is 2.
# Second window is [1, 1], count of distinct numbers is 1.
# Input: arr[] = [1, 1, 1, 1, 1], k = 3
# Output: [1, 1, 1]
# Explanation: Every window of size 3 in the array [1, 1, 1, 1, 1], contains only the element 1, so the number of distinct elements in each window is 1.

#1(not optimal)
class Solution:
    def countDistinct(self, arr, k):
        # code here
        res=[]
        for i in range(len(arr)-k+1):
            window=arr[i:i+k]
            unique=set(window)
            res.append(len(unique))
        return res
# However, it is not a moving-average formula specifically. It is a general formula for counting windows.
# Formula
# \[
# \text{Number of windows} = n-k+1
# \]

# Where:
# - n = Total number of elements.
# - k = Window size.
# - 1 = Includes the first window in the count.

#2(optimal)
class Solution:
    def countDistinct(self, arr, k):
        freq = {}
        res = []

        # Store frequencies of the first window
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1

        res.append(len(freq))

        # Move the window forward
        for i in range(k, len(arr)):

            # Remove the element leaving the window
            freq[arr[i - k]] -= 1

            # Delete the element if its frequency becomes zero
            if freq[arr[i - k]] == 0:
                del freq[arr[i - k]]

            # Add the new element entering the window
            freq[arr[i]] = freq.get(arr[i], 0) + 1

            # Store the distinct count of the current window
            res.append(len(freq))

        return res