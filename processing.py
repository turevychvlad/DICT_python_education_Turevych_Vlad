# Функція для зчитування матриці
def read_matrix(prompt):
    while True:
        try:
            rows, cols = map(int, input(prompt).split())
            if rows <= 0 or cols <= 0:
                raise ValueError("Розміри матриці мають бути додатніми.")
            break
        except ValueError as e:
            print(f"Неправильний ввід: {e}")

    print("Enter matrix:")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i + 1}: > ").split()))
                if len(row) != cols:
                    raise ValueError("Кількість елементів у рядку не відповідає заданій ширині матриці.")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Неправильний ввід: {e}")

    return matrix, rows, cols


# Функція для виведення матриці
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Функція для додавання матриць
def add_matrices():
    matrix_a, rows_a, cols_a = read_matrix("Enter size of first matrix: > ")
    matrix_b, rows_b, cols_b = read_matrix("Enter size of second matrix: > ")

    if rows_a != rows_b or cols_a != cols_b:
        print("The operation cannot be performed.")
        return

    result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(cols_a)] for i in range(rows_a)]
    print("The result is:")
    print_matrix(result)


# Функція для множення матриці на константу
def multiply_by_constant():
    matrix, rows, cols = read_matrix("Enter size of matrix: > ")
    while True:
        try:
            constant = float(input("Enter constant: > "))
            break
        except ValueError:
            print("Неправильний ввід: Константа має бути числом.")

    result = [[matrix[i][j] * constant for j in range(cols)] for i in range(rows)]
    print("The result is:")
    print_matrix(result)


# Функція для множення матриць
def multiply_matrices():
    matrix_a, rows_a, cols_a = read_matrix("Enter size of first matrix: > ")
    matrix_b, rows_b, cols_b = read_matrix("Enter size of second matrix: > ")

    if cols_a != rows_b:
        print("The operation cannot be performed.")
        return

    result = [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(cols_a)) for j in range(cols_b)] for i in range(rows_a)]
    print("The result is:")
    print_matrix(result)


# Функція для транспонування матриці
def transpose_matrix():
    matrix, rows, cols = read_matrix("Enter matrix size: > ")
    
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    while True:
        try:
            choice = int(input("Your choice: > "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError("Вибір має бути між 1 і 4.")
            break
        except ValueError as e:
            print(f"Неправильний ввід: {e}")

    if choice == 1:
        result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    elif choice == 2:
        result = [[matrix[rows - j - 1][cols - i - 1] for j in range(rows)] for i in range(cols)]
    elif choice == 3:
        result = [[matrix[i][cols - j - 1] for j in range(cols)] for i in range(rows)]
    elif choice == 4:
        result = [[matrix[rows - i - 1][j] for j in range(cols)] for i in range(rows)]

    print("The result is:")
    print_matrix(result)


# Функція для знаходження визначника матриці
def determinant(matrix):
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(size):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


# Функція для знаходження оберненої матриці
def inverse_matrix():
    matrix, rows, cols = read_matrix("Enter matrix size: > ")

    if rows != cols:
        print("This matrix doesn't have an inverse.")
        return

    det = determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    size = len(matrix)
    cofactors = [[((-1) ** (r + c)) * determinant(
                  [row[:c] + row[c + 1:] for row in (matrix[:r] + matrix[r + 1:])])
                  for c in range(size)] for r in range(size)]
    adjugate = [[cofactors[c][r] for c in range(size)] for r in range(size)]
    inverse = [[adjugate[r][c] / det for c in range(size)] for r in range(size)]

    print("The result is:")
    print_matrix(inverse)


# Головне меню
def main():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        while True:
            try:
                choice = int(input("Your choice: > "))
                if choice not in range(0, 7):
                    raise ValueError("Вибір має бути між 0 і 6.")
                break
            except ValueError as e:
                print(f"Неправильний ввід: {e}")

        if choice == 0:
            break
        elif choice == 1:
            add_matrices()
        elif choice == 2:
            multiply_by_constant()
        elif choice == 3:
            multiply_matrices()
        elif choice == 4:
            transpose_matrix()
        elif choice == 5:
            matrix, _, _ = read_matrix("Enter matrix size: > ")
            print("The result is:")
            print(determinant(matrix))
        elif choice == 6:
            inverse_matrix()


# Запуск програми
if __name__ == "__main__":
    main()
