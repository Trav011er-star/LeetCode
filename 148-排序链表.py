# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
# 归并排序天然适合链表（只需改指针，无需随机访问），本题常用两种写法：
#   解法一（sortList）        ：自顶向下递归归并，时间 O(n log n)，空间 O(log n)（递归栈）
#   解法二（sortListBottomUp）：自底向上迭代归并，时间 O(n log n)，空间 O(1)
# 两者共用 merge（合并两个有序链表）与 cut（切断一段子链）两个辅助操作。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        解法一：自顶向下归并排序（递归）
        1. 空链表或只有 1 个节点 -> 已经有序，直接返回（递归出口）
        2. 快慢指针找中点，把链表从中间断开成左右两半
        3. 递归排序左半、右半
        4. 用 _merge 合并两段有序链表

        时间 O(n log n)，空间 O(log n)（递归栈）

        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        # 快慢指针找中点：slow 最终停在左半段的最后一个节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 从中间断开，得到左半 head 与右半 mid
        mid = slow.next
        slow.next = None

        # 递归排序两半，再合并
        return self._merge(self.sortList(head), self.sortList(mid))

    def _merge(self, l1, l2):
        """合并两个升序链表，返回合并后的头节点（双指针，谁小接谁）。"""
        # 1 -> 3  2 -> 4
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next
