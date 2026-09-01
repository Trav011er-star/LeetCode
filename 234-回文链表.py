# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 先分两半
        if not head or not head.next:
            return True
        # 找到中点
        fast_node = head
        slow_node = head
        while fast_node is not None and fast_node.next is not None:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
        middle_node = slow_node

        # 反转后半部分
        prev_node = None
        current_node = slow_node
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        # 比较前半部分和后半部分
        current_node = head
        while current_node is not middle_node:
            first_half_val = current_node.val
            last_half_val = prev_node.val
            if first_half_val != last_half_val:
                return False
            current_node = current_node.next
            prev_node = prev_node.next

        return True


if __name__ == "__main__":
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next

    result = Solution().isPalindrome(head)
    print(result)  # True
