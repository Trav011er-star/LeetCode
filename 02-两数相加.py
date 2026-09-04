# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current1 = l1
        current2 = l2
        current = None
        plus = 0
        while current1 and current2:
            if not current:
                current = ListNode((current1.val + current2.val + plus) % 10)
                plus = (current1.val + current2.val + plus) / 10
                current1 = current1.next
                current2 = current2.next
                head = current
                continue
            current.next = ListNode((current1.val + current2.val + plus) % 10)
            plus = (current1.val + current2.val + plus) / 10
            current1 = current1.next
            current2 = current2.next
            current = current.next

        # l2 比较短
        while current1:
            current.next = ListNode((current1.val + plus) % 10)
            plus = (current1.val + plus) / 10
            current1 = current1.next
            current = current.next

        while current2:
            current.next = ListNode((current2.val + plus) % 10)
            plus = (current2.val + plus) / 10
            current2 = current2.next
            current = current.next

        if plus > 0:
            current.next = ListNode(plus)
            current = current.next

        return head
