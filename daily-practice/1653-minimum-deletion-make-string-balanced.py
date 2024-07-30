"""
1653. Minimum Deletions to make string balanced

Level: Medium

You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

 

Constraints:

    1 <= s.length <= 105
    s[i] is 'a' or 'b'​​.
"""

"""
Approach: Brute Force in O(n)

- Count all 'a's in string
- Iterate through while decrementing a_count to right after landing on 'a' elements
- Calculate deletions
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right = 0   #   Count of 'a's to right of element

        #   Total 'a's in s
        for c in s:
            a_count_right += 1 if c == "a" else 0

        #   Initialize for storing potential deletions required for balancing
        b_count_left = 0
        res = len(s)

        #    Iterate through string and update counts   
        for i, c in enumerate(s):
            if c == "a":
                a_count_right -= 1
            
            #   Sum of potential deletions
            res = min(res, b_count_left + a_count_right)
            if c == "b":
                b_count_left += 1
        
        return res