# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(next=head)
        current = dummy_head
        while True:
            current_rough = current
            is_reverse = True

            # 判断前面是否有 k 个节点可以反转
            for i in range(k):
                current_rough = current_rough.next
                if not current_rough:
                    is_reverse = False
                    break

            if is_reverse:
                # 反转小链的头
                current_head = current
                # 反转小链的尾
                current_tail = current_rough.next
                # 对中间的 k 个节点进行逆向
                dummy_head_sec = ListNode(next=current_head.next)
                # 小虚拟节点
                current_sec = dummy_head_sec
                # 1
                current1 = dummy_head_sec.next
                while not (current1 == current_tail):
                    # 2 3 4
                    current2 = current1.next

                    current1.next = current_sec
                    # 1 2 3
                    current_sec = current1
                    # 2 3 4
                    current1 = current2

                dummy_head_sec.next.next = current1
                current_head.next = current_sec

                # current 移动到当前组翻转后的尾节点
                current = dummy_head_sec.next

            # 说明剩下不足 k 个节点了，直接结束
            else:
                break
        return dummy_head.next
