class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        Areas = []
        p1 = 0
        p2 = len(height) - 1
        # 每次移动较短的那边，宽度变小，高度一定变大或不变
        # 如果两边一样长，移动任意一边，宽度变小，高度一定不变或变小
        # 总的来说，每次移动宽度一定变小，而高度一定是最优选择
        while p1 < p2:
            if height[p1] > height[p2]:
                current_height = height[p2]
                current_width = p2 - p1
                p2 -= 1
            else:
                current_height = height[p1]
                current_width = p2 - p1
                p1 += 1

            area = current_height * current_width
            Areas.append(area)

        return max(Areas)
