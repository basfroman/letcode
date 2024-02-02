# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be
# pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
#
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'[val: {self.val} (left: {self.left}, right: {self.right}]'


class Solution:
    # def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:
    #     def dfs(node: TreeNode, friq: dict[int, int]) -> int:
    #
    #         if node is None:
    #             return 0
    #
    #         friq[node.val] = friq.get(node.val, 0) + 1
    #
    #         if node.left is None and node.right is None:
    #             odd = sum(1 for i in friq.values() if i % 2)
    #             return 1 if odd < 2 else 0
    #
    #         return dfs(node.left, dict(friq)) + dfs(node.right, dict(friq))
    #
    #     return dfs(root, dict())
    def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:

        def dfs(node, p):
            if not node:
                return 0
            x = node.val
            p ^= (1 << x)
            print(x, p)
            if not node.left and not node.right:
                if p & (p - 1) == 0:
                    return 1
                return 0
            return dfs(node.left, p) + dfs(node.right, p)

        p = 0
        res = dfs(root, p)
        print('>', res)
        return res

def get_tree(values, index=0):
    if index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = get_tree(values, 2 * index + 1)
    root.right = get_tree(values, 2 * index + 2)

    return root

if __name__ == '__main__':
    sol = Solution()

    # root = [2,2,1]
    # tree = get_tree(root)
    # assert sol.pseudoPalindromicPaths(tree) == 1
    #
    # root = [2,3,1,3,1,None,1]
    # tree = get_tree(root)
    # assert sol.pseudoPalindromicPaths(tree) == 2
    #
    # root = [2,1,1,1,3,None,None,None,None,None,1]
    # tree = get_tree(root)
    # assert sol.pseudoPalindromicPaths(tree) == 2

    root = [2, 1, None, 2, None, 1]
    tree = get_tree(root)
    assert sol.pseudoPalindromicPaths(tree) == 0
