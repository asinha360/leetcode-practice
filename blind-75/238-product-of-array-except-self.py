"""
238. Product of Array Except Self

Level: Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

"""
Approach: Prefix * Postfix multiplication

Put all prefix and postfix products at every single position and put them in 2 arrays.


"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

"""
Solution Breakdown:

- Initialize array to [1, 1, 1, 1] so product of empty prefix | postfix = 1
- Start with prefix init to 1; iterate through nums; prefix *= nums[i] for each element at index i in prefix

    => so iteration 1 would have 1*1, iteration 2 would have 1*2, iteration 3 would have 2*3, iteration 4 would have 6*4

- take prefix array; init postfix to 1; iterate right to left; for elem at index i postfix *= res[i]; postfix *= nums[i]
"""