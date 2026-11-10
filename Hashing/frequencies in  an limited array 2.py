# Frequencies in a Limited Array
# Solved
# Difficulty: EasyAccuracy: 27.64%Submissions: 410K+Points: 2Average Time: 10m
# Given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

# Examples:

# Input: arr[] = [2, 3, 2, 3, 5]
# Output: [0, 2, 2, 0, 1]
# Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.
# Input: arr[] = [3, 3, 3, 3]
# Output: [0, 0, 4, 0]
# Explanation: We have: 1 occurring 0 times, 2 occurring 0 times, 3 occurring 4 times, and 4 occurring 0 times.
# Input: arr[] = [1]
# Output: [1]
# Explanation: We have: 1 occurring 1 time, and there are no other numbers between 1 and the size of the array.

class Solution:
    def frequencyCount(self, arr):
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        res=[]
        for i in range(1,len(arr)+1):#takes value from 1 to last element as it is considered as n+1
            res.append(freq.get(i,0))#if value inn dict use that value or uses the existing 0 in the freq.get()method
        return res