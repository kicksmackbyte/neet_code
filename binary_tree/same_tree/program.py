'''

# Prompt

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


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

        def _flatten(node, acc):

            if node:
                acc.append(node.val)
                _flatten(node.left, acc)
                _flatten(node.right, acc)

            else:
                acc.append(None)

            return acc


        p_flattened = _flatten(p, [])
        q_flattened = _flatten(q, [])

        return p_flattened == q_flattened


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
