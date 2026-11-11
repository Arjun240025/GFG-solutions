# All Pairs with Sum from 2 Arrays
# Solved
# Difficulty: EasyAccuracy: 23.94%Submissions: 184K+Points: 2Average Time: 15m
# Given two unsorted arrays a[]  and b[], the task is to find all pairs whose sum equals x from both arrays.

# Note: All pairs should be returned in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then (u1,v1) should be returned first else second.

# Examples:

# Input: target = 9, a[] = [1, 2, 4, 5, 7], b[] = [5, 6, 3, 4, 8]
# Output: 
# 1 8
# 4 5 
# 5 4
# Explanation: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.
# Input: target = 8, a[] = [-1, -2, 4, -6, 5, 7], b[] = [6, 3, 4, 0]
# Output:
# 4 4 
# 5 3
# Input: target = 9, a[] = [1, 2, 4, 5, 7, 4], b[] = [5, 6, 3, 4, 8, 4]
# Output:
# 1 8
# 4 5
# 4 5
# 5 4
# 5 4
# Explanation: (1, 8), (4, 5), (4, 5), (5, 4) and (5, 4) are the pairs which sum to 9.
class Solution:
    def allPairs(self, target, arr1, arr2):
        # code here 
        freq={}
        for i in arr2:
            freq[i]=freq.get(i,0)+1
        res=[]
        for i in arr1:
            need=target-i
            
            if need in freq:
                for j in range(freq[need]):
                    res.append([i,need])
        res.sort()
        return res
    

