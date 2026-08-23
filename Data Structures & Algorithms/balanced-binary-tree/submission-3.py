# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if not root:
                return 0
            leftH = getHeight(root.left)
            rightH = getHeight(root.right)
            if leftH == -2 or rightH == -2:
                return -2
            if abs(leftH - rightH) > 1:
                return -2
            height = max(leftH, rightH) + 1
            return height

        if getHeight(root) == -2:
            return False
        else:
            return True
        