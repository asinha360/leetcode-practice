"""840. Magic Squares in Grid

Level: Medium

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:

Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.

Example 2:

Input: grid = [[8]]
Output: 0

 

Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 10
    0 <= grid[i][j] <= 15
"""

class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def magic(r, c):

            values = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])

            for i in range(r, r + 2):
                if sum(grid[i][c:c+3]) != 15:
                    return 0
                
            for i in range(c, c + 3):
                if (grid[r][i] + grid[r + 1][i] + grid[r + 2][i] != 15):
                    return 0
            
            if (
                grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
                grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15
            ):
                return 0

            return 1 
        
        res = 0

        for r in range(ROWS - 2):
            for c in range(COLS - 2):

                res += magic(r, c)

        return res