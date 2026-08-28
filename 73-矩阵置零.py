class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        record_raw = set()
        record_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    record_raw.add(i)
                    record_col.add(j)

        for i in range(len(matrix)):
            if i in record_raw:
                # 要求用原地算法：直接修改输入的 matrix，不创建并返回一个新的矩阵
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
            else:
                for j in range(len(matrix[i])):
                    if j in record_col:
                        matrix[i][j] = 0

        return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    print(Solution().setZeroes(matrix))
