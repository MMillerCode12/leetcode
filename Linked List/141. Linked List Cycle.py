# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast != None:
            
            fast = fast.next

            if fast == None:
                return False

            fast = fast.next
            slow = slow.next

            if fast == None:
                return False
            elif fast == slow:
                return True

        return False    
