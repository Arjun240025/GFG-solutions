# Isomorphic Strings
# Solved
# Difficulty: EasyAccuracy: 34.21%Submissions: 250K+Points: 2Average Time: 30m
# Given two strings s1 and s2 consisting only of lowercase English letters and having the same length, check whether they are isomorphic. Two strings are isomorphic if:

# Each character in s1 must always map to the same character in s2.
# No two different characters in s1 can map to the same character in s2.
# A character may map to itself.
# Return true if s1 and s2 are isomorphic, otherwise return false.

# Examples:

# Input: s1 = "aab", s2 = "xxy"
# Output: true
# Explanation: Each character in s1 can be consistently mapped to a unique character in s2 (a -> x, b -> y).
# Input: s1 = "aab", s2 = "xyz"
# Output: false
# Explanation: Same character 'a' in s1 maps to two different characters 'x' and 'y' in s2.
# Input: s1 = "abc", s2 = "xxz"
# Output: false
# Explanation: Two different characters 'a' and 'b' in s1 maps with same character 'x' in s2. 

class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        map1={}
        map2={}
        for i in range (len(s1)):
            if s1[i] in map1:
                if map1[s1[i]]!=s2[i]:
                    return False
            else:
                map1[s1[i]]=s2[i]
        
            if s2[i] in map2:
                if map2[s2[i]]!=s1[i]:
                    return False
            else:
                map2[s2[i]]=s1[i]
        return True