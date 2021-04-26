class NumMatrix(object):
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.matrix = [[val for val in sub] for sub in matrix]
        self.sum_matrix = [[0 for i in range(0, self.cols + 1)] for j in range(0, self.rows + 1)]
    
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.update_sum(i + 1, j + 1, matrix[i][j])
        
    def update(self, row, col, val):
        self.update_sum(row + 1, col + 1, val - self.matrix[row][col])
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum_rect(row2 + 1, col2 + 1) - self.sum_rect(row2 + 1, col1) - self.sum_rect(row1, col2 + 1) + self.sum_rect(row1, col1)
    
    def update_sum(self, x, y, val):
        i = x
        while i <= self.rows:
            j = y
            while j <= self.cols:
                self.sum_matrix[i][j] += val
                j += (j & -j)
            i += (i & -i)

    def sum_rect(self, row, col):
        s = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                s += self.sum_matrix[i][j]
                j -= (j & -j)
            i -= (i & -i)

        return s