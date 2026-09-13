# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 给你一个二叉树的根节点 root ， 检查它是否轴对称。
        # 递归终点
        if not root:
            return True

        def isMirror(left, right):
            # 左右子树都为空，返回True
            if not left and not right:
                return True
            # 左右子树有一个为空，返回False
            if not left or not right:
                return False
            # 左右子树的值不相等，返回False
            if left.val != right.val:
                return False
            # 递归检查左子树的左子树和右子树的右子树，以及左子树的右子树和右子树的左子树是否对称
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)
