class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            # 如果前面是正数
            if current_sum >= 0:
                current_sum += nums[i]
            # 如果前面是负数
            else:
                current_sum = nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum
