class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        lens = []
        for num in nums_set:
            # 找序列的起点
            if num - 1 in nums_set:
                # 说明此时的 num 不是序列起点，舍去
                continue
            # 说明此时的 num 是序列的起点
            else:
                current_len = 1
                num = num + 1
                # 找到最长的 len
                while num in nums_set:
                    num = num + 1
                    current_len = current_len + 1

                lens.append(current_len)

        return max(lens) if len(lens) > 0 else 0
