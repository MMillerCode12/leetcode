# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode()
        temp_head = new_head
        current_node = head
        dist_vals = []

        while current_node != None:
            if current_node.val in dist_vals:
                current_node = current_node.next
            elif (current_node.next != None) and (current_node.val == current_node.next.val):
                dist_vals.append(current_node.val)
                temp_head.next = None
                current_node = current_node.next
            else:
                temp_head.next = current_node
                temp_head = temp_head.next
                current_node = current_node.next
      

        return new_head.next
