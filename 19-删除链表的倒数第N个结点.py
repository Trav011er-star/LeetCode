# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        node_dict = {}
        current = head
        i = 0
        while current:
            i += 1
            node_dict[i] = current
            current = current.next

        # 此时 i 代表总共有多少个节点
        # 删除第 i - n + 1 个节点
        # 如果只有一个节点
        if i == 1:
            return None

        # 删除第一个节点
        if i == n:
            return head.next

        current = node_dict[i - n]
        current.next = current.next.next
        return head
