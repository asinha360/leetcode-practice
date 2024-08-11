"""
1568. Minimum Number of Days to Disconnect Island

Level: Hard

You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

Refer to https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/ for examples

Example 1:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 30
    grid[i][j] is either 0 or 1.
"""

class Solution:
    def minDays(self, grid: list[list[int]]) -> int:

        ROWS ,COLS = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                return
            
            visit.add((r, c))
            neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            
            for nr, nc in neighbors:
                dfs(nr, nc,visit)

        def count_islands():
            visit = set()
            count = 0


            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] and (r, c) not in visit:
                        dfs(r, c, visit)
                        count += 1
            return count

        if count_islands() != 1:
            return 0
        
        for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 0:
                        continue
                    grid[r][c] = 0
                    
                    if count_islands() != 1:
                        return 1
                    grid[r][c] = 1
        return 2