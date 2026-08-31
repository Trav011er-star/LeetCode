# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_Node = None
        # 2
        current_Node = head
        while current_Node is not None:
            # 2
            next_Node = current_Node.next
            # 5 -> None
            current_Node.next = prev_Node
            # 5
            prev_Node = current_Node
            # 2
            current_Node = next_Node

        return prev_Node


if __name__ == "__main__":
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next

    result = Solution().reverseList(head)
    values = []
    while result is not None:
        values.append(result.val)
        result = result.next
    print(values)  # [5, 4, 3, 2, 1]
