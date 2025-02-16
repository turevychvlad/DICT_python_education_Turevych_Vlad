import random

def generate_simple_task():
    """
    Генерує просте арифметичне завдання: два випадкові числа від 2 до 9 та одну з операцій (+, -, *).
    """
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operation = random.choice(["+", "-", "*"])

    # Вираховуємо правильну відповідь
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return num1, operation, num2, correct_answer

def generate_square_task():
    """
    Генерує завдання на зведення в квадрат чисел від 11 до 29.
    """
    num = random.randint(11, 29)
    correct_answer = num ** 2
    return num, correct_answer

def get_valid_input():
    """
    Запитує користувача про відповідь, перевіряє правильність формату.
    """
    while True:
        answer = input("> ").strip()
        if answer.isdigit() or (answer.startswith('-') and answer[1:].isdigit()):
            return int(answer)
        print("Incorrect format.")

def arithmetic_test(level):
    """
    Проводить арифметичний тест залежно від рівня складності.
    """
    correct_answers = 0

    for _ in range(5):
        if level == 1:
            num1, operation, num2, correct_answer = generate_simple_task()
            print(f"{num1} {operation} {num2}")
        else:
            num1, correct_answer = generate_square_task()
            print(f"{num1}")

        user_answer = get_valid_input()

        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5.")
    return correct_answers

def save_result(correct_answers, level):
    """
    Запитує користувача, чи хоче він зберегти результат, та записує у файл.
    """
    print("Would you like to save your result to the file? Enter yes or no.")
    response = input("> ").strip().lower()

    if response in ["yes", "y"]:
        print("What is your name?")
        name = input("> ").strip()

        level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
        result_entry = f"{name}: {correct_answers}/5 in level {level} ({level_description}).\n"

        with open("results.txt", "a") as file:
            file.write(result_entry)

        print('The results are saved in "results.txt".')

def main():
    """
    Основна функція програми. Запитує рівень та запускає тест.
    """
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        level_input = input("> ").strip()

        if level_input in ["1", "2"]:
            level = int(level_input)
            break
        else:
            print("Incorrect format.")

    correct_answers = arithmetic_test(level)
    save_result(correct_answers, level)

if __name__ == "__main__":
    main()
