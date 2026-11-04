# Palindrome String
# Solved
# Difficulty: BasicAccuracy: 51.21%Submissions: 534K+Points: 1
# Given a string s, find if it is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

# Examples :

# Input: s = "abba"
# Output: true
# Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
# Input: s = "abc" 
# Output: false
# Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.


#1
class Solution:
    def isPalindrome(self, s):
        # code here
        if s[::]==s[::-1]:
            return True
        return False


#2(two pointer approach)
class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
