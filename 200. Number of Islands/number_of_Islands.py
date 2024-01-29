from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        counter = 0

        h = len(grid)
        w = len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= w or y < 0 or y >= h or grid[y][x] == '0':
                return
            grid[y][x] = '0'
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for y in range(h):
            for x in range(w):
                if grid[y][x] == '1':
                    counter += 1
                    dfs(x, y)

        return counter

if __name__ == '__main__':
    sol = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert(sol.numIslands(grid) == 1)

    grid = [
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert (sol.numIslands(grid) == 4)

    grid = []
    assert (sol.numIslands(grid) == 0)

    grid = [["1","1","0","1","0"]]
    assert sol.numIslands(grid) == 2
