# Given a random 5x5 grid of random letters, find all words formed by acyclically
# traversing edge-adjacent (left/right/above/below) squares, given the function
# bool isWord(string) that tells you whether a string is a word or not.


def isWords(word: str) -> bool:
   validWords = ["dog", "doggy", "cat", "zoo", 'roman', 'of']
   return word in validWords

grid = [
  ['r', 'o', 'u', 'x', 'w'],
  ['d', 'm', 'a', 'n', 'u'],
  ['c', 'd', 'c', 'a', 'h'],
  ['a', 'z', 'a', 'c', 'u'],
  ['o', 'f', 't', 'v', 'g']
]


memo = {}

def dfs(row, col, path):
    for dr, dc in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            print(grid[new_row][new_col])

            if isWords(''.join(path)):
                print('This is word:', ''.join(path))
            dfs(new_row, new_col, path + [grid[new_row][new_col]])


def find_words():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(i, j, [grid[i][j]])


if __name__ == '__main__':
    find_words()
