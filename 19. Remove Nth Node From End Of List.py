# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head
        list_length = 0

        while current_node:
            current_node = current_node.next
            list_length += 1

        if n == list_length:
            return head.next

        current_node = head

        for i in range(list_length - n - 1):
            current_node = current_node.next

        if current_node.next != None:
            current_node.next = current_node.next.next

        return head

