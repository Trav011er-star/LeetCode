"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy_head = Node(0)
        current_copy = dummy_head
        # 当前被复制的节点
        current = head
        node_dict = {}
        while current:
            # 如果这个节点不存在
            if current not in node_dict:
                current_copy.next = Node(current.val)
                node_dict[current] = current_copy.next
            # 这个节点已经复制过了
            else:
                current_copy.next = node_dict[current]
            current_copy = current_copy.next

            # 处理 random 的指向
            if not current.random:
                current_copy.random = None
                current = current.next
                continue

            if current.random not in node_dict:
                current_copy.random = Node(current.random.val)
                node_dict[current.random] = current_copy.random
            # 这个节点已经复制过了
            else:
                current_copy.random = node_dict[current.random]

            current = current.next

        return dummy_head.next
