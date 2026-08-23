# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxd = 0
    level = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.level += 1

        leftHeight = self.diameterOfBinaryTree(root.left)
        rightHeight = self.diameterOfBinaryTree(root.right)
        height = 1 + max(leftHeight, rightHeight)

        self.maxd = max(self.maxd, leftHeight + rightHeight)

        self.level -= 1

        if self.level == 0:
            return self.maxd
        else:
            return height
        return 
        
