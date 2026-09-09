class ListNode(object):
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev  # 添加 prev 属性，用于双向链表


class LRUCache(object):
    # 实现 LRUCache 类：
    # LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
    # int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    # void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
    # 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        # 双向链表
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # 将 key 移动到缓存的末尾，表示最近使用过
            # 把节点更新到最尾部
            current_node = self.cache[key]
            self.del_node(node=current_node)
            self.mov_to_tail(current_node)
            return current_node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 如果双向链表里原本有这个节点
        if key in self.cache:
            current_node = self.cache[key]
            current_node.val = value
            # 先删除当前节点
            self.del_node(node=current_node)
        else:
            current_node = ListNode(key, value)
            self.cache[key] = current_node

        # 把节点更新到最尾部
        self.mov_to_tail(node=current_node)

        if len(self.cache) > self.capacity:
            # 从双向链表中删除最前的节点
            oldest_node = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

            # 字典中逐出最久未使用的关键字
            del self.cache[oldest_node.key]

    def del_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def mov_to_tail(self, node):
        old_node = self.tail.prev
        old_node.next = node
        node.prev = old_node
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # 缓存是 {1=1}
    lRUCache.put(2, 2)  # 缓存是 {1=1, 2=2}
    print(lRUCache.get(1))  # 返回 1
    lRUCache.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    print(lRUCache.get(2))  # 返回 -1 (未找到)
    lRUCache.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    print(lRUCache.get(1))  # 返回 -1 (未找到)
    print(lRUCache.get(3))  # 返回 3
    print(lRUCache.get(4))  # 返回 4
