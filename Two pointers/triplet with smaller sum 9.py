# Triplets with Smaller Sum
# Solved
# Difficulty: MediumAccuracy: 40.33%Submissions: 140K+Points: 4
# Given an array arr[] of distinct integers and an integer sum, count the number of unique triplets of elements whose sum is strictly less than sum. A triplet is identified only by the three elements it contains, so different permutations of the same three elements are counted as one triplet.

# Examples :

# Input: sum = 2, arr[] = [-2, 0, 1, 3]
# Output:  2
# Explanation: Triplets with sum less than 2 are (-2, 0, 1) and (-2, 0, 3). 
# Input: sum = 12, arr[] = [5, 1, 3, 4, 7]
# Output: 4
# Explanation: Triplets with sum less than 12 are (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).

class Solution:
    def countTriplets(self, sum, arr):
        #code here
        arr.sort()  # Sort the array
        count = 0

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total < sum:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count
#     2. Why right - left?
# 	Because the array is sorted, if the largest possible third element (9) gives a sum smaller than 16, then the other elements between left and right will also give smaller sums.

# 	Let's check:
# 	Triplet	Sum	Valid?
# 	2 + 3 + 5	10	Yes
# 	2 + 3 + 7	12	Yes
# 	2 + 3 + 9	14	Yes

# 	There are 3 valid triplets.

# Why not count += 1?

# Because that would count only the current triplet and miss the other valid combinations.

# That's the main trick in the Triplets with Smaller Sum problem!