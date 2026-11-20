# Union of 2 Sorted Arrays
# Solved
# Difficulty: MediumAccuracy: 31.39%Submissions: 584K+Points: 4Average Time: 20m
# Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order. Union of two arrays can be defined as the set containing distinct elements that are present in either of the arrays.

# Examples:

# Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
# Output: [1, 2, 3, 4, 5, 6, 7]
# Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
# Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
# Output: [1, 2, 3, 4, 5]
# Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.
# Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
# Output: [1, 2]
# Explanation: Distinct elements including both the arrays are: 1 2.


        
        
        
class Solution:
    def findUnion(self, a, b):
        i=0
        j=0
        res=[]
        while i<len(a) and j<len(b):
            if a[i] < b[j]:#for if a element is lesser than b element so that appends element in a in sorted order
                if not res or res[-1]!=a[i]:
                    res.append(a[i])
                i+=1
            elif a[i]>b[j]:#for if b element is lesser than a element so that appenda that element in b in sorted order
                if not res or res[-1]!=b[j]:
                    res.append(b[j])
                j+=1
            else:#for if both the elements in the a and b are equal
                if not res or res[-1]!=a[i]:
                    res.append(a[i])
                i+=1
                j+=1
        while i < len(a):#if all elemnts are compared one to one and causes to one array to be completed so that it checks both trheconditions and append the remaining elments in the array a or b by checking the below two while loops
            if not res or res[-1]!=a[i]:
                res.append(a[i])
            i+=1
        while j < len(b):
            if not res or res[-1]!=b[j]:
                res.append(b[j])
            j+=1
        return res