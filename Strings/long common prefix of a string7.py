# Longest Common Prefix of Strings
# Solved
# Difficulty: EasyAccuracy: 29.52%Submissions: 335K+Points: 2Average Time: 15m
# Given an array of strings arr[]. Return the longest common prefix among each and every strings present in the array. If there's no prefix common in all the strings, return "".

# Examples :

# Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
# Output: "gee"
# Explanation: "gee" is the longest common prefix in all the given strings.
# Input: arr[] = ["hello", "world"]
# Output: ""
# Explanation: There's no common prefix in the given strings.

class Solution:
    def longestCommonPrefix(self, arr):
        prefix=arr[0]
        for i in arr[1:]:#starts from index 1 to n
            while not i.startswith(prefix):#check  every array element starts with prefix if not  eliminate last char of the current prefix
                prefix=prefix[:-1]#eliminate until the prefix becomes almost to the next array element then consider next array element
                
                if prefix == "":#for if nothinh startswith prefix (for false condition)
                    return ""
        return prefix