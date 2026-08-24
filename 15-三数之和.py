class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                current_sum = nums[i] + nums[p1] + nums[p2]

                # 三数之和小了，需要增大，向右移动 p1
                if current_sum < 0:
                    p1 += 1
                    # 因为本来就不满足，把重复的移动掉，使三数和一定增大
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1

                # 三数之和大了，需要减小，向左移动 p2
                elif current_sum > 0:
                    p2 -= 1
                    # 因为本来就不满足，把重复的移动掉，使三数和一定减小
                    while p2 > p1 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1

                else:
                    result.append([nums[i], nums[p1], nums[p2]])
                    p2 -= 1
                    p1 += 1
                    # 因为已经满足了，遍历一样的数字没有意义
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1

                    while p2 > p1 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1

        return result
