# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        else:
            return 1 + self.helperCount(root)
    
    def helperCount(self, nextNode):
        
        if (not nextNode) or (not nextNode.right and not nextNode.left):
            return 0
        elif nextNode.left and not nextNode.right:
            return 1
        else:
            return 2 + self.helperCount(nextNode.right) + self.helperCount(nextNode.left)
