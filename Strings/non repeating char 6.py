# Non Repeating Character
# Solved
# Difficulty: EasyAccuracy: 40.43%Submissions: 364K+Points: 2Average Time: 30m
# Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.

# Examples:

# Input: s = "geeksforgeeks"
# Output: 'f'
# Explanation: In the given string, 'f' is the first character in the string which does not repeat.
# Input: s = "racecar"
# Output: 'e'
# Explanation: In the given string, 'e' is the only character in the string which does not repeat.
# Input: s = "aabbccc"
# Output: '$'
# Explanation: All the characters in the given string are repeating.

class Solution:
    def nonRepeatingChar(self,s):
        count={}
        for i in s:
            count[i]=count.get(i,0)+1#count every char and add it to the dictionary
        for i in s:
            if count[i]==1:
                return i#using the previously counted dict return the first char that appears for the first time
        return '$'

       #.get() method is used to retrieve the value associated with a key in a dictionary. It takes two arguments: the key to look up and an optional default value to return if the key is not found. In this case, count.get(i, 0) retrieves the current count of the character i from the count dictionary. If i is not present in the dictionary, it returns 0 as the default value. This allows us to increment the count of each character in the string s without raising a KeyError for characters that haven't been encountered yet.