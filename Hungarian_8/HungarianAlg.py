import numpy as np


class HungarianAlg:
    def __init__(self, cost_matrix):
        self.cost_matrix = np.array(cost_matrix)
        self.n = self.cost_matrix.shape[0]  # Assuming cost_matrix is square
        self.marked = np.zeros_like(self.cost_matrix, dtype=int)  # 0: unmarked, 1: starred, 2: primed
        self.row_covered = np.zeros(self.n, dtype=bool)
        self.col_covered = np.zeros(self.n, dtype=bool)
        self.path = []

    def solve(self):
        self.__reduce_matrix()
        self.__star_zeros()
        while not self.__cover_columns():
            self.__prime_and_adjust()

        # Extract the optimal assignment
        return [(r, int(np.where(self.marked[r] == 1)[0][0])) for r in range(self.n)]

    def __reduce_matrix(self):
        # Step 1: Subtract the smallest value in each row
        for i in range(self.n):
            self.cost_matrix[i] -= self.cost_matrix[i].min()
        # Step 2: Subtract the smallest value in each column
        for j in range(self.n):
            self.cost_matrix[:, j] -= self.cost_matrix[:, j].min()

    def __star_zeros(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.cost_matrix[i, j] == 0 and not self.row_covered[i] and not self.col_covered[j]:
                    self.marked[i, j] = 1  # Star the zero
                    self.row_covered[i] = True
                    self.col_covered[j] = True
        # Reset covers
        self.row_covered[:] = False
        self.col_covered[:] = False

    def __cover_columns(self):
        # Cover columns with starred zeros
        for j in range(self.n):
            if 1 in self.marked[:, j]:
                self.col_covered[j] = True
        return self.col_covered.sum() == self.n

    def __prime_and_adjust(self):
        while True:
            # Step 4: Find a non-covered zero and prime it
            row, col = self.__find_uncovered_zero()
            if row is None:  # If no such zero exists, adjust the matrix
                self.__adjust_matrix()
                continue
            self.marked[row, col] = 2  # Prime the zero

            # Step 5: Check if there is a starred zero in the same row
            if 1 in self.marked[row]:
                star_col = np.where(self.marked[row] == 1)[0][0]
                self.row_covered[row] = True
                self.col_covered[star_col] = False
            else:
                # Step 6: Construct the alternating path and convert primes to stars
                self.__augment_path(row, col)
                # Reset covers and primes
                self.row_covered[:] = False
                self.col_covered[:] = False
                self.marked[self.marked == 2] = 0
                return

    def __find_uncovered_zero(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.cost_matrix[i, j] == 0 and not self.row_covered[i] and not self.col_covered[j]:
                    return i, j
        return None, None

    def __augment_path(self, row, col):
        self.path = [(row, col)]
        while True:
            star_col = np.where(self.marked[:, self.path[-1][1]] == 1)[0]
            if len(star_col) == 0:
                break
            self.path.append((star_col[0], self.path[-1][1]))

            prime_row = np.where(self.marked[self.path[-1][0]] == 2)[0][0]
            self.path.append((self.path[-1][0], prime_row))

        # Flip stars and primes along the path
        for r, c in self.path:
            if self.marked[r, c] == 1:
                self.marked[r, c] = 0
            elif self.marked[r, c] == 2:
                self.marked[r, c] = 1

    def __adjust_matrix(self):
        # Find the smallest uncovered value
        min_val = np.min(self.cost_matrix[~self.row_covered][:, ~self.col_covered])
        # Subtract it from all uncovered elements
        for i in range(self.n):
            for j in range(self.n):
                if not self.row_covered[i] and not self.col_covered[j]:
                    self.cost_matrix[i, j] -= min_val
                elif self.row_covered[i] and self.col_covered[j]:
                    self.cost_matrix[i, j] += min_val