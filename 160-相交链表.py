# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        current_A = headA
        current_B = headB
        A_set = set()
        B_set = set()
        while current_A is not None or current_B is not None:
            if current_A is not None:
                # A 当前节点曾经被 B 访问过
                if current_A in B_set:
                    return current_A

                A_set.add(current_A)
                current_A = current_A.next

            if current_B is not None:
                # B 当前节点曾经被 A 访问过
                if current_B in A_set:
                    return current_B

                B_set.add(current_B)
                current_B = current_B.next

        return
