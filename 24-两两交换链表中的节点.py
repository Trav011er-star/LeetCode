# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 先保存好链表头
        dummy_head = ListNode(next=head)

        if not head or not head.next:
            return head

        current = dummy_head
        while current.next and current.next.next:
            current_head = current
            current = current.next
            next_node = current.next
            current.next = next_node.next
            next_node.next = current
            current_head.next = next_node

        return dummy_head.next
