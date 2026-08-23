# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depth = 0
    maxd = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.depth += 1
        self.maxd = max(self.depth, self.maxd)
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        self.depth -= 1
        return self.maxd