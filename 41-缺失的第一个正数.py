class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
        # 输入：nums = [1,2,0]
        # 输出：3
        # 解释：范围 [1,2] 中的数字都在数组中。

        # 方法一
        # nums_set = set(nums)
        # min_num = min(nums)
        # max_num = max(nums)

        # if min_num > 1 or max_num <= 0:
        #     return 1

        # for i in range(1, len(nums) + 1):
        #     if i not in nums_set:
        #         return i

        # return max_num + 1

        nums_set = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                return i

        return len(nums) + 1


if __name__ == "__main__":
    nums = [1, 2, 0]
    nums = [3, 4, -1, 1]
    nums = [7, 8, 9, 11, 12]

    print(Solution().firstMissingPositive(nums))
