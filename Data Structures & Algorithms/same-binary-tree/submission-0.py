# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True
        def dfs(p, q):
            if not self.isSame:
                return
            if not p or not q:
                if not (p == None and q == None):
                    self.isSame = False
                return
            if p.val != q.val:
                self.isSame = False
                return
            dfs(p.left, q.left)
            dfs(p.right, q.right)
            return
        
        dfs(p, q)
        return self.isSame


        