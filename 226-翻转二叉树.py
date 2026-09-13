# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
        # 左右节点交换

        # 递归终点
        if not root:
            return
        root_left = root.left
        root_right = root.right
        root.left = root_right
        root.right = root_left

        # 翻转左子树
        self.invertTree(root.left)
        # 翻转右子树
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    # 构建二叉树
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    solution = Solution()
    root = solution.invertTree(root)

    # 输出翻转后的二叉树的根节点值
    print(root.left.val)  # 输出: 7
