# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow, fast = head.next, head.next.next
        
        while fast and fast.next and slow != fast:
            slow, fast = slow.next, fast.next.next
        
        if fast != slow:
            return None

        slow = head
        while slow and fast.next and slow != fast:
            slow, fast = slow.next, fast.next

        return slow