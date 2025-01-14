'''

# Prompt

The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree.
The path does not necessarily have to pass through the root.
The length of a path between two nodes in a binary tree is the number of edges between the nodes.
Given the root of a binary tree root, return the diameter of the tree.


# Constraints

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


'''

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0
        def _helper(node):

            nonlocal diameter

            if node:

                left_height = _helper(node.left)
                right_height = _helper(node.right)

                diameter = max(diameter, left_height + right_height)

                return 1 + max(left_height, right_height)

            else:
                return 0


        _helper(root)
        return diameter


e = TreeNode(5)
d = TreeNode(4)
c = TreeNode(3, e)
b = TreeNode(2, c, d)
a = TreeNode(1, None, b)

solution = Solution()
answer = solution.diameterOfBinaryTree(a)

assert answer == 3, f'Expected: {3}, Got: {answer}'
