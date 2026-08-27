class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
        # 输出：[[1,6],[8,10],[15,18]]
        # 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

        result = []
        # 先按区间的起始位置排序
        intervals.sort(key=lambda x: x[0])
        # lambda 方法：
        # function = lambda input: output

        for i in range(len(intervals)):
            print(f"result = {result}")
            print(f"当前处理{intervals[i]}")
            if not result:
                result.append(intervals[i])
                continue

            # 下一个区间的左和已经合并好的区间的右相比较
            # 如果下一个区间的左在已合并好的区间的右的里面，说明这两个区间要合并
            print(f"对比{intervals[i][0]}和{result[-1][1]}")
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
                continue

            else:
                # 如果下一个区间的左不在已合并好的区间的右的里面，说明要新增一个区间
                result.append(intervals[i])

        return result


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    s = Solution()
    print(s.merge(intervals))
