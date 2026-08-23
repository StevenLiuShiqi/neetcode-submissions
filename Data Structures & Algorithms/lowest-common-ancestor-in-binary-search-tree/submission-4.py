# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    def isChild(self, root, p, array:list):
        if not root:
            return False
        array.append(root)
        if root.val == p.val:
            return True
        if self.isChild(root.left, p, array) or self.isChild(root.right, p, array):
            return True
        array.pop()
        return False


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pArray = []
        qArray = []
        findp, findq = self.isChild(root, p, pArray), self.isChild(root, q, qArray)
        if not findp or not findq:
            return None
        counter = 0
        while counter < min(len(pArray), len(qArray)):
            if pArray[counter] != qArray[counter]:
                return pArray[counter - 1]
            counter += 1
        
        return pArray[counter - 1]
        
        pass