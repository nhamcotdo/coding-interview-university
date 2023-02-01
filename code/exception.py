# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1 = 0
        idx1 = 0

        curr1 = l1
        while curr1 != None:
            sum1 += curr1.val * 10 ** idx1
            curr1 = curr1.next
            idx1 += 1
        sum2 = 0
        idx2 = 0

        curr2 = l2
        while curr2 != None:
            sum2 += curr2.val * 10 ** idx2
            curr2 = curr2.next
            idx2 += 1

        sum = str(sum1 + sum2)

        rs = None
        for i in range(len(sum)):
            new_rs = ListNode(int(sum[i]), rs)
            rs = new_rs
        
        return rs

            

