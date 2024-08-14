"""
719. Find K-th Smallest Pair Distance

Level: Hard

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:

Input: nums = [1,1,1], k = 2
Output: 0

Example 3:

Input: nums = [1,6,1], k = 3
Output: 5

 

Constraints:

    n == nums.length
    2 <= n <= 104
    0 <= nums[i] <= 106
    1 <= k <= n * (n - 1) / 2
"""

class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:

        nums.sort()

        def helper(dist):

            L = 0
            res = 0

            for R in range(len(nums)):
                while nums[R] - nums[L] > dist:
                    L += 1
                res += R - L
            return res
        
        L, R = 0, max(nums)

        while L < R:
            M = L + ((R - L) // 2)
            pairs = helper(M)

            if pairs >= k:
                R = M
            else:
                L = M + 1
        return R