# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 深度等于左右子树的最大深度 + 1（当前节点）
        # 递归终点
        if not root:
            return 0
        # 左右子树的最大深度 + 1（当前节点）
        height1 = self.maxDepth(root.left) + 1
        # 右子树的最大深度 + 1（当前节点）
        height2 = self.maxDepth(root.right) + 1
        return max(height1, height2)


if __name__ == "__main__":
    # 构建二叉树
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.maxDepth(root))  # 输出: 3
