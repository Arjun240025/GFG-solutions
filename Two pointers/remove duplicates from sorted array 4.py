# Remove Duplicates Sorted Array
# Solved
# Difficulty: EasyAccuracy: 38.18%Submissions: 410K+Points: 2Average Time: 20m
# You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.

# Examples :

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: After removing all the duplicates only one instance of 2 will remain i.e. [2] so modified array will contains 2 at first position and you should return array containing [2] after modifying the array.
# Input: arr[] = [1, 2, 4]
# Output: [1, 2, 4]
# Explanation:  As the array does not contain any duplicates so you should return [1, 2, 4].

class Solution:
    def removeDuplicates(self, arr):
        left=0
        for right in range(1,len(arr)):
            if arr[left]!=arr[right]:
                left+=1
                arr[left]=arr[right]
        return arr[:left+1]
        
        # Remember:
        # - left += 1 → Moves to the next position available for a unique element.
        # - arr[left] = arr[right] → Copies the newly found unique element into that position.
        # Why not just arr[:left]?
        # Because slicing excludes the ending index.

        # If we use arr[:2], we get [1, 2] and miss 3.