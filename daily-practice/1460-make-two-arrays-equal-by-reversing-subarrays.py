"""
1460. Make Two Arrays Equal by Reversing Subarrays

Level: Easy

You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.

Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.

Example 3:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.

 

Constraints:

    target.length == arr.length
    1 <= target.length <= 1000
    1 <= target[i] <= 1000
    1 <= arr[i] <= 1000
"""

"""
Approach: Hashmap: Both approaches are in O(n) using hashmaps and counters to rearrange lists to see if they can be reversed since if the count of each element is the same, this will always be true.
"""

from collections import defaultdict

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:

        # return Counter(target) == Counter(arr)

        count1, count2 = defaultdict(int), defaultdict(int)
        
        for n1, n2 in zip(target, arr):
            count1[n1] += 1
            count2[n2] += 1

        if len(count1) != len(count2):
            return False
        
        for n in count1:
            if count1[n] != count2[n]:
                return False
        
        return True
        

    def canBeEqualAlt (self, target: list[int], arr: list[int]) -> bool:
        count = defaultdict(int)
    
        for n1, n2 in zip(target, arr):
            count[n1] += 1
            count[n2] -= 1

        for n in count:
            if count[n] != 0:
                return False
        
        return True