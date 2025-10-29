from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_0 = any(x == 0 for x in matrix[0])
        col_0 = any(x[0] == 0 for x in matrix)
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0

        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0

        if row_0:
            for j in range(m):
                matrix[0][j] = 0
        if col_0:
            for i in range(n):
                matrix[i][0] = 0
