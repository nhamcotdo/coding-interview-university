# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next or not head.next.next:
            return

        # find mid
        mid = last = head
        while last and last.next:
            mid = mid.next
            last = last.next.next
        #reverse
        new_mid = mid
        while mid and mid.next:
            next_mid = mid.next
            mid.next = next_mid.next
            next_mid.next = new_mid
            new_mid = next_mid
        mid = new_mid
        #order
        _head = head
        while mid and mid.next:
            mid_next = mid.next
            mid.next = _head.next
            _head.next = mid
            _head = mid.next
            mid = mid_next
            