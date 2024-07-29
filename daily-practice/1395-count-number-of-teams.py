"""
1395. Count Number of Teams

Level: Medium

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4

 

Constraints:

    n == rating.length
    3 <= n <= 1000
    1 <= rating[i] <= 105
    All the integers in rating are unique.
"""

"""
Approach: Greedy Algorithm - Initially Dynamic Programming but memory and space complexity too high
"""

class Solution:
    def numTeams(self, rating: list[int]) -> int:
        res = 0 #   Stores count of valid teams

        #   Iterate through each index as 'middle'
        for m in range(1, len(rating) - 1):
            left_smaller = right_larger = 0

            #   Calculate valid elements to left of m
            for i in range(m):
                if rating[i] < rating[m]:
                    left_smaller += 1
            
            #   Calculate valid elements to right of m
            for i in range(m + 1, len(rating)):
                if rating[i] > rating[m]:
                    right_larger += 1

            #   Valid teams with rating in increasing order
            res += left_smaller * right_larger

            #   Valid teams with rating in decreasing order after subtracting from previously calculated teams
            left_larger = m - left_smaller
            right_smaller = len(rating) - m - 1 - right_larger

            #   Valid teams with rating in both correct orders. ie rating[i] > rating[j] > rating[k] + rating[i] < rating[j] < rating[k]
            res += left_larger * right_smaller

        return res