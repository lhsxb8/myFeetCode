class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        Len = len(matrix)
        for i in range(Len):
            for j in range(i+1):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return 

