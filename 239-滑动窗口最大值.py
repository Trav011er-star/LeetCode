from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = deque()
        result = []
        for i in range(len(nums)):
            window_right = i
            window_left = window_right - k + 1

            # 跟最右边的值比较,若新进来的值比之前的值大，就不必保存之前的值的索引
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            # 移动后，把队列中已经移走的值对应索引去掉
            # 此时队列中只剩下比当前遍历到的 num[i] 大的数
            while queue and queue[0] < window_left:
                queue.popleft()

            queue.append(i)

            if i >= k - 1:
                result.append(nums[queue[0]])

        return result


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 1, 1, 3]
    print(solution.maxSlidingWindow(nums=nums, k=3))
