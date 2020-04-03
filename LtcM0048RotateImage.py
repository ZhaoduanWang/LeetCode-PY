class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        print(n)
        for i in range(n):
            for j in range(n):
                col = (n-1-i)
                print(f'[{i}][{j}]{matrix[i][j]} -> [{j}][{col}]')
                # ? can't clone a matrix res, then put temp into clone matrix
                # temp = matrix[i][j];
                # res[j][col] = temp;

matrix1 = [ [1,2,3],
            [4,5,6],
            [7,8,9] ]

matrix2 = [ [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13,3, 6,  7],
            [15,14,12,16] ]
sol = Solution()
sol.rotate(matrix1)

