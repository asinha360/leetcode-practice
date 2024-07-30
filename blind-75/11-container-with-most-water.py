"""
11. Container with Most Water

Level: Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Reference image @ https://leetcode.com/problems/container-with-most-water/description/

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""

"""
Approach: Two pointer in O(n)
"""

class Solution:
    #   Brute Force Approach
    def maxAreaBrute(self, height: list[int]) -> int:
        res = 0

        for L in range(len(height)):
            for R in range(L + 1, len(height)):
                area = (R - 1) * min(height[L], height[R])
                res = max(res, area)

        return res
    
    #   Optimal Approach - O(n)
    def maxAreaOptimal(self, height: list[int]) -> int:
        res = 0
        L, R = 0, len(height) - 1   #   Pointers at opposite ends of list

        #   Calculate area as distance between pointers * height of shorter line
        while L < R:
            area = (R - L) * min(height[L], height[R])
            res = max(res, area)

            #   Move pointers if height of L < R or L > R - whichever is smaller is moved in the direction of the other
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return res