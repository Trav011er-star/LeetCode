class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
        # 输出：true
        # 每行的元素从左到右升序排列。
        # 每列的元素从上到下升序排列。

        m = len(matrix)
        n = len(matrix[0])

        # 方法一
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] > target:
        #             break
        #         if matrix[i][j] == target:
        #             return True

        # 方法二（右上角）
        for i in range(m):
            if matrix[i][n - 1] == target:
                return True
            elif matrix[i][n - 1] > target:
                for j in range(n - 2, -1, -1):
                    if matrix[i][j] == target:
                        return True
            # 如果比当前行最右侧的值大，那当前行其他数字也不用看了，开始看下一行

        return False


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 5
    print(Solution().searchMatrix(matrix, target))
