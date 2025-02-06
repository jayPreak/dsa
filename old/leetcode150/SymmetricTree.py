# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.checkSym(root.left, root.right)
    
    def checkSym(self, node1, node2):
        if not node1 and not node2:
            return True
        elif node1 and node2 and node1.val == node2.val:
            return self.checkSym(node1.left, node2.right) and self.checkSym(node1.right, node2.left)
        else:
            return False
