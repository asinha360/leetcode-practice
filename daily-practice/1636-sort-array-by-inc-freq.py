"""
1636. Sort Array by Increasing Frequency

Level: Easy

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Example 1:

    Input: nums = [1,1,2,2,2,3]
    Output: [3,1,1,2,2,2]
    Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:

    Input: nums = [2,3,1,3,2]
    Output: [1,3,3,2,2]
    Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:

    Input: nums = [-1,1,-6,4,5,-6,1,4,1]
    Output: [5,-1,4,4,-6,-6,1,1,1]

Constraints:

    1 <= nums.length <= 100
    -100 <= nums[i] <= 100
"""

"""
Preliminary Thinking: "Built-in Sort based on custom key"

    1) Loop through array + Create a hashmap (dict) with key being element and value being frequency
    2) Sort arr starting with minimal frequency value elements
    3) If frequency same: larger key sorts first

Actual Approach: For same frequency elements multiply by -1 so that it sorts its in descending order for those elements by default.

Counter is a dict subclass for counting hashable objects where elements are stored as dict keys and their counts as values.

"""

from collections import Counter

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        # Counter creates dict-like object 'count' where keys are elements form 'nums' and values are frequencies
        count = Counter(nums)

        # Returns tuple with 2 elements for each element in 'nums'. This determines order of elements in sorted list. 'count[n]' is the frequency of element 'n' while '-n' is just the negative.

            # Python sorts a list of tuples by the first element of each tuple, and if equal; by the second element.

            # 'count[n]' ensures ascending order for lower frequencies, while '-n' ensures decreasing order where frequencies are same.
        def custom_sort(n):
            return (count[n], -n)
        

        nums.sort(key=custom_sort)

        return nums

# From NeetCodeIO's youtube video @ https://www.youtube.com/watch?v=Evq1SfUbhBg

class betterSolution:
    def frequencySortBetter(self, nums: list[int]) -> list[int]:
        count = Counter(nums)

        def custom_sort(n):
            return (count[n], -n)
        

        nums.sort(key=lambda n: (count[n], -n))

        return nums
    
"""
Example solution progression:

List:

    nums = [1, 1, 2, 2, 2, 3]

Frequency Count:

    count = Counter(nums)
    # count = {1: 2, 2: 3, 3: 1}

Custom Sort:

    For 1: (count[1], -1) -> (2, -1)
    For 2: (count[2], -2) -> (3, -2)
    For 3: (count[3], -3) -> (1, -3)

Tuples Generated:

    [(2, -1), (2, -1), (3, -2), (3, -2), (3, -2), (1, -3)]

Primary: By the first element (frequency):

    (1, -3) comes first because it has the smallest frequency.
    Next, the pairs (2, -1) and (3, -2) are sorted by their frequencies.

Secondary: For tuples with the same frequency, by the second element (-n):

    Among (2, -1) pairs, they remain in the same order since their secondary sorting criteria are the same.
    Similarly, (3, -2) pairs remain in the same order.

Final sorted order of tuples:

[(1, -3), (2, -1), (2, -1), (3, -2), (3, -2), (3, -2)]

Sorted List Result:

[3, 1, 1, 2, 2, 2]
"""