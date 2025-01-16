'''

# Prompt

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Constraints

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


'''

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root:

            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            if left > right:
                return 1 + left
            else:
                return 1 + right

        else:
            return 0
