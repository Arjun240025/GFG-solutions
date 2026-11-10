# Check for Subsequence
# Solved
# Difficulty: EasyAccuracy: 51.68%Submissions: 99K+Points: 2
# Given two strings s1 and s2. You have to check that s1 is a subsequence of s2 or not.
# Note: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

# Examples:

# Input: s1 = "AXY", s2 = "YADXCP"
# Output: false
# Explanation: s1 is not a subsequence of s2 as 'Y' appears before 'A'.
# Input: s1 = "gksrek", s2 = "geeksforgeeks"
# Output: true
# Explanation: If we combine the bold character of "geeksforgeeks", it equals to s1. So s1 is a subsequence of s2. 

#two pointer
class Solution:
    def isSubSeq(self, s1, s2):
        j=0
        for i in s2:
            if j<len(s1) and s1[j]==i:#since j must be equal to the length of s1, we check if j is less than the length of s1. If it is, we check if the character at index j in s1 is equal to the current character in s2. If they are equal, we increment j to move to the next character in s1.
                j+=1
        return j ==len(s1)