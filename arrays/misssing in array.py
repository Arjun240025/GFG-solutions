# Missing in Array
# Solved
# Difficulty: EasyAccuracy: 29.59%Submissions: 1.8MPoints: 2Average Time: 15m
# You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

# Examples:

# Input: arr[] = [1, 2, 3, 5]
# Output: 4
# Explanation: All the numbers from 1 to 5 are present except 4.
# Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
# Output: 6
# Explanation: All the numbers from 1 to 8 are present except 6.
# Input: arr[] = [1]
# Output: 2
# Explanation: Only 1 is present so the missing element is 2.

class Solution:
    def missingNum(self, arr):
        # code here
            n=len(arr)+1
            tot=0
            for i in range(1,n+1):#Here, range(n) starts at 0 and stops before n. So, when n = 5, i takes the values 0, 1, 2, 3, 4.
                                  #You missed 5!
                                  #That's why we use range(1, n + 1) to include every number from 1 through n.
                tot+=i
            arrs=sum(arr)#sum of arrays method is used to find the sum of all the elements in the array. It takes the array as input and returns the total sum of its elements.
            return tot - arrs