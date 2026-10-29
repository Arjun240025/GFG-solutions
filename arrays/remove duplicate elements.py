# Remove Duplicates Sorted Array
# Difficulty: EasyAccuracy: 38.18%Submissions: 409K+Points: 2Average Time: 20m
# You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.

# Examples :

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: After removing all the duplicates only one instance of 2 will remain i.e. [2] so modified array will contains 2 at first position and you should return array containing [2] after modifying the array.
# Input: arr[] = [1, 2, 4]
# Output: [1, 2, 4]
# Explanation:  As the array does not contain any duplicates so you should return [1, 2, 4].

#1 (not a good solution a lot of time complexity)
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        res=[]
        for i in arr:
            if i not in res:
                res.append(i)
        return res


#2 (better solution)
class Solution:
    def removeDuplicates(self, arr):
        res = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] != res[-1]:
                res.append(arr[i])

        return res
    

# My Understanding of This Program
# First, we declare a variable called res to store the first element of the array, which is arr[0]. We store this first element because we want to keep one copy of every distinct element in the result.
# Next, we use for i in range(1, len(arr)) to loop through the array, starting from the second element and continuing until the last element. We skip the first element because we have already stored it in res.
# Inside the loop, we check the condition if arr[i] != res[-1]. Here, arr[i] represents the current element we are checking, and res[-1] represents the last element currently present in the result list.
# If the current element is not equal to the last element of res, it means we have found a new distinct element. So, we append the current element to res using res.append(arr[i]).
# But if the current element is equal to the last element of res, it means the element is already present as the most recently stored distinct value. Since the array is sorted, duplicate elements appear next to each other, so we can simply skip that element without appending it.
# Finally, we return res, which contains all the distinct elements in their original order.