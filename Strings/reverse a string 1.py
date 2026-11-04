# Reverse a String
# Solved
# Difficulty: BasicAccuracy: 69.49%Submissions: 624K+Points: 1Average Time: 15m
# Given a string s, reverse the string.

# Examples:

# Input: s = "Geeks"
# Output: "skeeG"
# Input: s = "for"
# Output: "rof"
# Input: s = "a"
# Output: "a"

#1
class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        return s[::-1]

#2
class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        # return s[::-1]
        res = list(s)  # Converts the string into a list of characters
        res.reverse()  # Reverses the list in place
        return "".join(res)  # Joins the characters into a string
    