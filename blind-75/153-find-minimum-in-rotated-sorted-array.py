"""
153. Find Minimum in Rotated Sorted Array

Level: Medium

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

 

Constraints:

    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.
"""

"""
Approach: Binary Search - O(log n)

- Use L and R pointers with M being the middle pointer to figure out which sorted portion you're in - if middle value is in the right sorted portion; search in left portion
- nums[m] >= nums[L] - will tell you which is the sorted portion relative to M
- shift left pointer all the way to M+1
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]   #   Initialized to first element in array
        L, R = 0, len(nums) - 1 #   Initialized to leftmost and rightmost elements in array

        #   Check if array is already sorted where L < R and update res to smaller value between res and nums[L] to reflect min value
        while L <= R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break
            
            #   Calculate and update middle element
            M = (L + R) // 2
            res = min(res, nums[M])

            #   Main search to check which side of the array is sorted relative to the middle element
            if nums[M] >= nums[L]:
                L = M + 1   #   Search the right part of array
            else:
                R = M - 1   #   Search the left part of array
        return res  #   min value of array
