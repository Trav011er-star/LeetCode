class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        """
        i=0         j:0->n-1
        i:0->m-1    j=n-1
        i=m-1       j:n-1->0
        i:m-1->m-2  j=0
        i=m-2       j:0->n-2
        """

        """
        1   2   3   4   5
        10  9   8   7   6
        11  12  13  14  15
        20  19  18  17  16
        """

        m = len(matrix)
        n = len(matrix[0])
        length = m * n
        # 四条边界
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        result = []

        while True:
            # 正
            # i=0         j:0->n-1
            print(f"遍历列 {left} -> {right}")
            for j in range(left, right + 1, 1):
                result.append(matrix[top][j])
            top += 1
            if len(result) == length:
                return result

            # i:0->m-1    j=n-1
            print(f"遍历行 {top} -> {bottom}")
            for i in range(top, bottom + 1, 1):
                result.append(matrix[i][right])
            right -= 1
            if len(result) == length:
                return result

            # 反
            # i=m-1       j:n-1->0
            print(f"遍历列 {right} -> {left}")
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            if len(result) == length:
                return result

            # i:m-1->m-2  j=0
            print(f"遍历行 {bottom} -> {top}")
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if len(result) == length:
                return result


if __name__ == "__main__":
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(Solution().spiralOrder(matrix))
