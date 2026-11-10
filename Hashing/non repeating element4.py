# Non-Repeating Element
# Difficulty: EasyAccuracy: 39.31%Submissions: 164K+Points: 2Average Time: 20m
# Find the first non-repeating element in a given array arr of integers and if there is not present any non-repeating element then return 0

# Note: The array consists of only positive and negative integers and not zero.

# Examples:

# Input: arr[] = [-1, 2, -1, 3, 2]
# Output: 3
# Explanation: -1 and 2 are repeating whereas 3 is the only number occuring once. Hence, the output is 3. 
# Input: arr[] = [1, 1, 1]
# Output: 0
# Explanation: There is not present any non-repeating element so answer should be 0.

class Solution:
    def firstNonRepeating(self, arr): 
        # code here
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for i in range(len(arr)):
            if freq[arr[i]]==1:
                return arr[i]
        return 0