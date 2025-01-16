'''

# Prompt

Given a binary tree, determine if it is height-balanced.


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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        nodes_balanced = True

        def _height(node):

            nonlocal nodes_balanced

            if node and nodes_balanced:

                left = _height(node.left)
                right = _height(node.right)

                nodes_balanced = (1 >= (left - right) >= -1)

                max_height = max(left, right)
                return 1 + max_height

            else:
                return 0

        if root:

            left_height = _height(root.left)
            right_height = _height(root.right)

            return (nodes_balanced) and (1 >= (left_height - right_height) >= -1)

        else:
            return True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def _helper(root):

            if root:

                l_balanced, l_height = _helper(root.left)
                r_balanced, r_height = _helper(root.right)

                balanced = (l_balanced and r_balanced) and (1 >= l_height-r_height >= -1)
                max_height = max(l_height, r_height)

                return (balanced, 1 + max_height)

            else:

                return (True, 0)

        balanced, height = _helper(root)
        return balanced


g = TreeNode(4, None, None)
f = TreeNode(4, None, g)
e = TreeNode(3, f, None)
d = TreeNode(3, None, e)
c = TreeNode(2, None, None)
b = TreeNode(2, d, None)
a = TreeNode(1, b, c)

root = a

solution = Solution()
answer = solution.isBalanced(root)

assert not(answer)
