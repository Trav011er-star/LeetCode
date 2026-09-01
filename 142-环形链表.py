# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        current = head

        while current is not None:
            if current in seen:
                return current
            seen.add(current)
            current = current.next

        return


def main():
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3  # 构造环：5 -> 3

    result = Solution().detectCycle(head)
    print(result.val)  # 3


if __name__ == "__main__":
    main()
