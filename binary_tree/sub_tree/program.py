'''

# Prompt

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.


# Constraints

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4


'''

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def _helper(node_1, node_2):

            if node_1 and node_2:

                if node_1.val == node_2.val:
                    return _helper(node_1.left, node_2.left) and _helper(node_1.right, node_2.right)
                else:
                    return False

            else:
                return node_1 == node_2

        return _helper(p, q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        elif not root:
            return False

        elif self.isSameTree(root, subRoot):
            return True

        else:
            a = self.isSubtree(root.left, subRoot)
            b = self.isSubtree(root.right, subRoot)

            return (a or b)
