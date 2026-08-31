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
        current = head
        length = 1
        while current is not None:
            current = current.next
            length += 1

        begin = length / 2 if length%2==0 else (length + 1)/2

        # 1->2 4->5 begin = 3
        for i in range(begin-1):





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