class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 输入: nums = [1,2,3,4]
        # 右侧乘积 [24,12,4,1]
        # 左侧乘积 [1,1,2,6]
        # 输出: [24,12,8,6]

        # 分别计算左右侧的所有乘积
        left_mul = [1] * len(nums)
        right_mul = [1] * len(nums)
        all_mul = []

        for i in range(1, len(nums)):
            # 右侧乘积
            right_mul[-i - 1] = right_mul[-i] * nums[-i]
            # print(f"right_mul = {right_mul}")

            # 左侧乘积
            left_mul[i] = left_mul[i - 1] * nums[i - 1]
            # print(f"left_mul = {left_mul}")

        all_mul = [right_mul[i] * left_mul[i] for i in range(len(nums))]
        return all_mul


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(Solution().productExceptSelf(nums))
