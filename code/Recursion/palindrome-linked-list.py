# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # find the mid
        mid = last = head
        while last and last.next:
            mid = mid.next
            last = last.next.next
        
        def reverse(head):
            temp = head
            while temp and temp.next:
                temp_next = temp.next
                temp.next = temp_next.next
                temp_next.next = head
                head = temp_next

            return head
        
        def compare(head, mid):
            if not head or not mid:
                return True
            
            return head.val == mid.val and compare(head.next, mid.next)
        
        mid = reverse(mid)

        ans = compare(head, mid)

        reverse(mid)

        return ans

        
        