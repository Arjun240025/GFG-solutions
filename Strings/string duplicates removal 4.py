# String Duplicates Removal
# Solved
# Difficulty: EasyAccuracy: 58.68%Submissions: 255K+Points: 2Average Time: 15m
# Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.

# Examples:

# Input: s = "geEksforGEeks"
# Output: "geEksforG"
# Explanation: After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".
# Input: s = "HaPpyNewYear"
# Output: "HaPpyNewYr"
# Explanation: After removing duplicate characters such as e, a, we have string as "HaPpyNewYr".

class Solution:
    def removeDuplicates(self, s):
        b = ""  # empty string
        for i in s:
            if i not in b:
                b += i#use operators for strings
        return b


#         Quick comparison
# Method	Used with	Purpose
# +=	String, List	Add or concatenate
# .add()	Set	Add a unique element
# .append()	List	Add one element
# .extend()	List	Add multiple elements