class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
	# 返回类型
        :rtype: List[int]
        """
	# value : i
        nums_set = {}
	
	# 枚举
        for i,num1 in enumerate(nums):
            num2 = target - num1
            if num2 in nums_set:
                return [nums_set[num2],i]

            nums_set[num1] = i

        