# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def tree_while(root, low, high):
            if not root:
                return 0
            if low <= root.val <= high:
                return root.val + tree_while(root.left, low, high) + tree_while(root.right, low, high)
            else:
                return tree_while(root.left, low, high) + tree_while(root.right, low, high)

        return tree_while(root, low, high)


if __name__ == '__main__':
    sol = Solution()
    assert sol.rangeSumBST(
        TreeNode(10,
                 TreeNode(5,
                          TreeNode(3), TreeNode(7)
                          ),
                 TreeNode(15,
                          None, TreeNode(18)
                          )
                 ),
        7, 15) == 32

