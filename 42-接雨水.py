class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 关键是计算每个柱子上的雨水
        # 这取决于每个柱子：
        # 左边最高柱子 = left_max
        # 右边最高柱子 = right_max
        # 且水面由较矮的一边决定

        # 只移动当前最大值较矮的那边
        # 即使另一边的柱子不是最高的，肯定也比当前移动的这边的柱子高，水面也取决于较低的柱子
        # 移动时也随时更新左右的最高柱子
        pool_volume = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max > right_max:
                right -= 1
                right_max = max(height[right], right_max)
                pool_volume += right_max - height[right]
            else:
                left += 1
                left_max = max(height[left], left_max)
                pool_volume += left_max - height[left]

        return pool_volume
