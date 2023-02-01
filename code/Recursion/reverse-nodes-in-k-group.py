# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def lenNodes(head):
            temp, length = head, 0
            while temp:
                length += 1
                temp = temp.next

            return length

        if lenNodes(head) < k:
            return head

        new_head, count = head, k - 1

        while head and head.next and count:
            count -= 1
            temp = head.next
            head.next = temp.next
            temp.next = new_head
            new_head = temp

        head.next = self.reverseKGroup(head.next, k)

        return new_head


# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         def lenNodes(head):
#             temp, length = head, 0
#             while temp:
#                 length += 1
#                 temp = temp.next

#             return length

#         l = lenNodes(head)

#         ans = head

#         for i in range(l//k):
#             new_head, count = head, k - 1
#             while head and head.next and count:
#                 count -= 1
#                 temp = head.next
#                 head.next = temp.next
#                 temp.next = new_head
#                 new_head = temp

#             if not i:
#                 ans = new_head
#                 tail = head
#             else:
#                 tail.next = new_head
#                 tail = head

#             head = head.next

#         return ans
