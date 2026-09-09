# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 我的做法
# class Solution(object):

#     def mergeKLists(self, lists):
#         """
#         :type lists: List[Optional[ListNode]]
#         :rtype: Optional[ListNode]
#         """

#         dummy_head = ListNode()
#         current = dummy_head
#         nums = []

#         for i in range(len(lists)):
#             if lists[i]:
#                 nums.append(lists[i].val)

#         while lists:
#             min_index, min_value = min(enumerate(nums), key=lambda item: item[1])
#             current.next = lists[min_index]
#             current = current.next
#             lists[min_index] = lists[min_index].next
#             if lists[min_index]:
#                 nums[min_index] = lists[min_index].val
#             else:
#                 del nums[min_index]
#                 del lists[min_index]

#         return dummy_head

import heapq


# 最小堆
# 最小堆会自动调整，保证每次取出来的都是最小的元素
# heap[0] 永远是最小的元素
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        min_heap = []

        # 将每条非空链表的头节点放入最小堆
        for list_index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, list_index, node))

        dummy_head = ListNode()
        current = dummy_head

        while min_heap:
            # 取出值最小的节点
            value, list_index, node = heapq.heappop(min_heap)

            # 连接到结果链表
            current.next = node
            current = current.next

            # 将该链表的下一个节点放入堆
            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_index, node.next))

        return dummy_head.next


def main():
    # 举例子作为验证
    # 创建链表1: 1 -> 4 -> 5
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    # 创建链表2: 1 -> 3 -> 4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    # 调用mergeKLists方法
    solution = Solution()
    merged_list = solution.mergeKLists([l1, l2])
    print("合并后的链表:")
    # 打印合并后的链表
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next


if __name__ == "__main__":
    main()
