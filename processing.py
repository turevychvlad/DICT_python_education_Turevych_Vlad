# файл для обробки матриць

def read_matrix():
    # читаємо матрицю
    try:
        rows, cols = map(int, input("Введіть кількість рядків і стовпців матриці: ").split())
        matrix = []
        for _ in range(rows):
            row = list(map(float, input("Введіть рядок матриці: ").split()))
            if len(row) != cols:
                raise ValueError("Невідповідна кількість елементів у рядку!")
            matrix.append(row)
        return matrix
    except Exception as e:
        print(f"Помилка при введенні матриці: {e}")
        return None

def add_matrices():
    # додаємо матриці
    try:
        print("Перша матриця:")
        matrix_a = read_matrix()
        print("Друга матриця:")
        matrix_b = read_matrix()

        if not matrix_a or not matrix_b:
            raise ValueError("Матриці не зчитані.")

        if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
            raise ValueError("Розміри матриць не співпадають.")

        result = []
        for i in range(len(matrix_a)):
            row = [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
            result.append(row)

        print("Результат додавання матриць:")
        for row in result:
            print(" ".join(map(str, row)))

    except Exception as e:
        print(f"Помилка при додаванні матриць: {e}")

def multiply_by_constant():
    # множимо матрицю на константу
    try:
        matrix = read_matrix()
        if not matrix:
            raise ValueError("Матриця не зчитана.")

        const = float(input("Введіть константу для множення: "))

        result = [[element * const for element in row] for row in matrix]

        print("Результат множення матриці на константу:")
        for row in result:
            print(" ".join(map(str, row)))

    except Exception as e:
        print(f"Помилка при множенні на константу: {e}")

def multiply_matrices():
    # множимо матриці
    try:
        print("Перша матриця:")
        matrix_a = read_matrix()
        print("Друга матриця:")
        matrix_b = read_matrix()

        if not matrix_a or not matrix_b:
            raise ValueError("Матриці не зчитані.")

        if len(matrix_a[0]) != len(matrix_b):
            raise ValueError("Кількість стовпців першої матриці не дорівнює кількості рядків другої.")

        result = []
        for i in range(len(matrix_a)):
            row = []
            for j in range(len(matrix_b[0])):
                value = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
                row.append(value)
            result.append(row)

        print("Результат множення матриць:")
        for row in result:
            print(" ".join(map(str, row)))

    except Exception as e:
        print(f"Помилка при множенні матриць: {e}")

def main():
    while True:
        try:
            print("""
1. Додавання матриць
2. Множення матриці на константу
3. Множення матриць
0. Вихід
            """)
            choice = input("Ваш вибір: ").strip()

            if choice == "1":
                add_matrices()
            elif choice == "2":
                multiply_by_constant()
            elif choice == "3":
                multiply_matrices()
            elif choice == "0":
                print("Вихід з програми.")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Помилка в головному меню: {e}")

if __name__ == "__main__":
    main()
