# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current1 = list1
        current2 = list2
        head_result = ListNode()
        current_result = head_result

        while current1 and current2:
            if current1.val > current2.val:
                current_result.next = current2
                current2 = current2.next
                current_result = current_result.next
            else:
                current_result.next = current1
                current1 = current1.next
                current_result = current_result.next
        if current1 is None:
            current_result.next = current2
            return head_result.next
        if current1 is None:
            current_result.next = current1
            return head_result.next


def main():
    # 创建两个升序链表
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # 合并链表
    result = Solution().mergeTwoLists(list1, list2)

    # 打印合并后的链表
    current = result
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    main()
