'''

# Prompt

Given the root of a binary tree, invert the tree, and return its root.


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

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:

            self.invertTree(root.left)
            self.invertTree(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp

        return root
