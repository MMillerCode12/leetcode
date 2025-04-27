# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_stack = []
        final_traversal = []
        continue_traversal = True
        
        if root != None:
            current_node = root
        else:
            return []

        while continue_traversal:
            if current_node is not None:
                inorder_stack.append(current_node)
                current_node = current_node.left
            elif len(inorder_stack) > 0:
                current_node = inorder_stack.pop(-1)
                final_traversal.append(current_node.val)
                current_node = current_node.right
            else:
                break

        return final_traversal
