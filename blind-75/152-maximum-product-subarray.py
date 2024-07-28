"""
152. Maximum Product Subarray

Level: Medium

Given an integer array nums, find a
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

 

Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

"""
Approach: Dynamic Programming Problem

Time Complexity = O(n)
Space Complexity = O(1)
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums) #   Will store max value found
        curMin, curMax = 1, 1   #   track min and max products of subarray ending at current position

        for n in nums:
            if n == 0:  #   Handle edge case where if n = 0, min and max product are both set to 1 and loop continues
                curMin, curMax = 1, 1
                continue
            
            tmp = curMax * n    #   Stores product of current number and previous max product
            curMax = max(n * curMax, n * curMin, n) #   Stores product of current number and previous min product
            curMin = min(tmp, n * curMin, n)    #   Stored the same way using tmp instead
            res = max(res, curMax)  #   Max value between current and previous max
        return res