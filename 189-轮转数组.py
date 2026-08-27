from collections import deque

# 方法一
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """

#         # 输入: nums = [1,2,3,4,5,6,7], k = 3
#         # 输出: [5,6,7,1,2,3,4]

#         # 利用双向队列
#         queue = deque(nums)
#         for i in range(k):
#             # 从右侧吐一个数字出来
#             num = queue.pop()
#             # 插入到左边
#             queue.appendleft(num)

# nums = list(queue)    # nums 指向新列表，原列表不变
# nums[:] = list(queue) # 替换原列表中的所有元素
# nums[:] = list(queue)


# 方法二（超时了，数组切片的本质上是复制，复杂度高）
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """

#         # 输入: nums = [1,2,3,4,5,6,7], k = 3
#         # 输出: [5,6,7,1,2,3,4]
#         # 防止输入的 k 超级大，造成无意义的轮转
#         k %= len(nums)

#         for i in range(k):
#             num = nums[-1]

#             nums[1:] = nums[:-1]
#             nums[0] = num

#         return nums


# 方法三
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """

#         # 输入: nums = [1,2,3,4,5,6,7], k = 3
#         # 输出: [5,6,7,1,2,3,4]

#         def reverse(nums, start_index, ended_index):
#             while start_index < ended_index:
#                 num = nums[start_index]
#                 nums[start_index] = nums[ended_index]
#                 nums[ended_index] = num
#                 start_index += 1
#                 ended_index -= 1

#         # 防止输入的 k 超级大，造成无意义的轮转
#         k %= len(nums)
#         nums.reverse()
#         reverse(nums, 0, k - 1)
#         reverse(nums, k, len(nums) - 1)

#         return nums


# 方法四
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 输入: nums = [1,2,3,4,5,6,7], k = 3
        # 输出: [5,6,7,1,2,3,4]

        # 防止输入的 k 超级大，造成无意义的轮转
        k %= len(nums)

        # 左开右闭
        # Python 的列表 list，+ 表示拼接（合并），并返回一个新列表
        nums[:] = nums[-k:] + nums[:-k]

        return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(Solution().rotate(nums, k))
