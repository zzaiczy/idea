class Solution:
    def rotate1(self, matrix):
        n = len(matrix)
        delta = n//2
        if not n % 2:
            even = 1
        else:
            even = 0
        # 旋转下去再提上来
        for i in range(n):
            for j in range(n):
                pass
        for i in range(1, delta+1):
            for j in range(1, delta+1):
                first_i, first_j = i+delta-1, j+delta-1
                second_i, second_j = j+delta-1, -i+delta-1
                third_i, third_j = -i+delta-1, -j+delta-1
                fourth_i, four_j = -j+delta-1, i+delta-1
                print(first_i, first_j, second_i, second_j, third_i, third_j, fourth_i, four_j)
                matrix[first_i][first_j], matrix[second_i][second_j], matrix[third_i][third_j], matrix[fourth_i][four_j] = matrix[fourth_i][four_j], matrix[first_i][first_j], matrix[second_i][second_j], matrix[third_i][third_j]
        return matrix


a = Solution()
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[1, 2], [3, 4]]
print(a.rotate1(c))
