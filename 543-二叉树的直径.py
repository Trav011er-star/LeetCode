# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.max_diameter


if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    # Construct a binary tree and call solution.diameterOfBinaryTree(root)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(solution.diameterOfBinaryTree(root))
