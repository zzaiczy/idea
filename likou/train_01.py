# 矩阵的旋转
class Solution:
    def rotate1(self, matrix):
        n = len(matrix)
        delta = n//2
        if n % 2:
            odd = 1
            tk = 0
        else:
            odd = 0
            delta = 2*delta
            tk = 1
        for i in range(1, delta+1, tk+1):
            for j in range(tk, delta+1, tk+1):
                first = [i, j]
                second = [j, -i]
                third = [-i, -j]
                fourth = [-j, i]
                first_i, first_j = (first[0]+delta-tk)//(tk+1), (first[1]+delta-tk)//(tk+1)
                second_i, second_j = (second[0]+delta-tk)//(tk+1), (second[1]+delta-tk)//(tk+1)
                third_i, third_j = (third[0]+delta-tk)//(tk+1), (third[1]+delta-tk)//(tk+1)
                fourth_i, four_j = (fourth[0]+delta-tk)//(tk+1), (fourth[1]+delta-tk)//(tk+1)
                matrix[first_i][first_j], matrix[second_i][second_j], matrix[third_i][third_j], matrix[fourth_i][four_j] = matrix[fourth_i][four_j], matrix[first_i][first_j], matrix[second_i][second_j], matrix[third_i][third_j]
        return matrix


a = Solution()
b = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(a.rotate1(b))
