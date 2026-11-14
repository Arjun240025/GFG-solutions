# Longest Consecutive Subsequence
# Solved
# Difficulty: MediumAccuracy: 33.0%Submissions: 424K+Points: 4Average Time: 25m
# Given an array arr[] of non-negative integers. Find length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

# Examples:

# Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
# Output: 6
# Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
# Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
# Output: 4
# Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.
# Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
# Output: 7
# Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.

class Solution:
    def longestConsecutive(self, arr):
        seen = set(arr)  # Store all elements for faster searching

        maximum = 0

        for i in seen:

            # Start counting only if the previous number is absent
            if i - 1 not in seen:
                count = 1
                num = i

                # Check whether the next consecutive number exists
                while num + 1 in seen:
                    num += 1
                    count += 1

                maximum = max(maximum, count)

        return maximum