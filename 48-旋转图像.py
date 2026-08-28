class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        # 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        """
        第一行 -> 第四列
        第二行 -> 第三列
        。。。
        """
        origin_matrix = [[0] * len(matrix)] * len(matrix)
        print(origin_matrix)
        # 逐行复制，避免内部列表仍指向同一位置
        for i in range(len(matrix)):
            # 行
            for j in range(len(matrix)):
                # 列
                origin_matrix[i][j] = matrix[i][j]
        print(origin_matrix)

        for i in range(len(matrix)):
            # 行
            for j in range(len(matrix)):
                # 列
                matrix[j][len(matrix) - i - 1] = origin_matrix[i][j]
                print(
                    f"{origin_matrix[i][j]} - ({i},{j}) - ({j},{len(matrix) - i - 1})"
                )

        return matrix


if __name__ == "__main__":
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    print(Solution().rotate(matrix))
