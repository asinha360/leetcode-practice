"""
2134. Minimum Swaps to Group All 1's Together II

Level: Medium

A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 

Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.

Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.

Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.

 

Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""
"""
Approach: Sliding Window
"""

class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        
        N = len(nums)
        total_ones = nums.count(1)
        L = 0
        window_ones = max_window_ones = 0

        #   Iterate through list twice due to circular nature
        for R in range(2 * N):
            if nums[R % N]: #   Check if current element is 1
                window_ones += 1
            if R - L + 1 > total_ones:  #   check if window size (R - L) is larger than number of ones; if yes move L to right
                window_ones -= nums[L % N]
                L += 1
            max_window_ones = max(max_window_ones, window_ones)
        return total_ones - max_window_ones