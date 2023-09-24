# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix():
    """Сложение, сравнение, умножение матриц"""

    def __init__(self, matrix: list):
        """Проверяет, матрица ли передана в параметрах"""
        self.count_els = []
        for i in matrix:
            self.count_els.append(len(i))
        if len(set(self.count_els)) == 1:
            self.matrix = matrix
            self.matrix_cols = len(matrix[0])
            self.matrix_rows = len(matrix)
        else:
            raise BaseException("Не матрица")

# def res_matrix_sample(self):
#     res_matrix = [0] * self.matrix_rows
#     for i in range(self.matrix_rows):
#         res_matrix[i] = [0] * self.matrix_cols
#     return res_matrix

    def __add__(self, other):
        """Складывает матрицы"""
        if isinstance(other, Matrix):
            if self.matrix_cols == other.matrix_cols and self.matrix_rows == other.matrix_rows:
                res_matrix = [0] * self.matrix_rows
                for i in range(self.matrix_rows):
                    res_matrix[i] = [0] * self.matrix_cols
                # self.res_matrix_sample()
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        res_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                return res_matrix
            else:
                raise TypeError('Невозможно сложить матрицы разного размера')
        # else:
        #     raise TypeError('Нужна матрица')

    def __eq__(self, other):
        """Сравнивает матрицы"""
        if isinstance(other, Matrix):
            if self.matrix_cols == other.matrix_cols and self.matrix_rows == other.matrix_rows:
                for i in range(self.matrix_rows):
                    for j in range(len(self.matrix[0])):
                        if self.matrix[i][j] == other.matrix[i][j]:
                            continue
                        else:
                            return False
                return True
            else:
                raise TypeError('Невозможно сравнить матрицы разного размера')
        # else:
        #     raise TypeError('Нужна матрица')

    def __mul__(self, other: int):
        """Перемножает матрицы или матрицу на число"""
        if isinstance(other, Matrix):
            if self.matrix_cols == other.matrix_rows:
                res_matrix = [0] * self.matrix_rows
                for i in range(self.matrix_rows):
                    res_matrix[i] = [0] * other.matrix_cols
                for i in range(other.matrix_cols):
                    for j in range(self.matrix_rows):
                        for k in range(self.matrix_cols):
                            res_matrix[j][i] += self.matrix[j][k] * other.matrix[k][i]
                return res_matrix
            else:
                raise TypeError('Количество столбцов первой матрицы должно быть равно количеству строк второй,'
                                'иначе матрицы не перемножить')
        elif str(other).isdigit():
            res_matrix = [0] * self.matrix_rows
            for i in range(self.matrix_rows):
                res_matrix[i] = [0] * self.matrix_cols
            # res_matrix_sample()
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    res_matrix[i][j] = self.matrix[i][j]*other
            return res_matrix
        # else:
        #     raise TypeError

    def __repr__(self):
        """Вывод инфо на печать для программиста"""
        return f'Matrix({self.matrix})'

    def __str__(self):
        """Вывод инфо на печать для пользователя"""
        return f'{self.matrix = }'

m = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

n = Matrix([[1, 2, 3, 2],
            [4, 5, 1, 2],
            [7, 8, 1, 3]])

# print(m + n)
print(m * n)
z = 5
print(m * z)
# print(m == n)
print(m.__repr__())
print(m.__str__())
print(Matrix.__doc__)
print(help(Matrix))