class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        # 计算前缀和
        current_sum = 0
        prefix_dict = {}
        prefix_dict[0] = 1

        for num in nums:
            current_sum += num
            current_need = current_sum - k
            if current_need in prefix_dict:
                count += prefix_dict[current_need]

            # 先判断之前的前缀和是否满足，再把当前的前缀和放进去
            # 否则如果 k = 0，会误把当前的前缀和计入
            if current_sum in prefix_dict:
                prefix_dict[current_sum] += 1
            else:
                prefix_dict[current_sum] = 1

        return count
