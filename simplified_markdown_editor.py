import sys

# Список доступних форматувальників
FORMATTERS = {
    "plain", "bold", "italic", "header", "link", "inline-code",
    "ordered-list", "unordered-list", "new-line"
}

# Спеціальні команди
SPECIAL_COMMANDS = {"!help", "!done"}

# Буфер для збереження розмітки
markdown_content = []


def print_help():
    """Виводить список доступних форматувальників і команд"""
    print("Available formatters:", " ".join(FORMATTERS))
    print("Special commands:", " ".join(SPECIAL_COMMANDS))


def format_plain():
    """Форматує звичайний текст без додаткового форматування"""
    text = input("Text: ")
    return text


def format_bold():
    """Форматує текст у напівжирний"""
    text = input("Text: ")
    return f"**{text}**"


def format_italic():
    """Форматує текст у курсив"""
    text = input("Text: ")
    return f"*{text}*"


def format_header():
    """Форматує заголовок з рівнем від 1 до 6"""
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                break
            print("The level should be within the range of 1 to 6.")
        except ValueError:
            print("Invalid input. Enter a number from 1 to 6.")

    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def format_link():
    """Форматує посилання у вигляді [Label](URL)"""
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def format_inline_code():
    """Форматує текст у вигляді інлайн-коду"""
    text = input("Text: ")
    return f"`{text}`"


def format_new_line():
    """Додає новий рядок"""
    return "\n"


def format_list(is_ordered):
    """Форматує список (упорядкований або невпорядкований)"""
    while True:
        try:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            print("The number of rows should be greater than zero.")
        except ValueError:
            print("Invalid input. Enter a positive integer.")

    result = []
    for i in range(1, rows + 1):
        row_text = input(f"Row #{i}: ")
        prefix = f"{i}. " if is_ordered else "* "
        result.append(f"{prefix}{row_text}")

    return "\n".join(result) + "\n"


def save_to_file():
    """Зберігає вміст у файл output.md"""
    with open("output.md", "w", encoding="utf-8") as file:
        file.write("\n".join(markdown_content))


def main():
    """Основна логіка програми"""
    while True:
        command = input("Choose a formatter: ").strip()

        if command == "!help":
            print_help()
            continue

        if command == "!done":
            save_to_file()
            sys.exit()

        if command not in FORMATTERS:
            print("Unknown formatting type or command")
            continue

        # Викликаємо відповідну функцію форматування
        if command == "plain":
            markdown_content.append(format_plain())
        elif command == "bold":
            markdown_content.append(format_bold())
        elif command == "italic":
            markdown_content.append(format_italic())
        elif command == "header":
            markdown_content.append(format_header())
        elif command == "link":
            markdown_content.append(format_link())
        elif command == "inline-code":
            markdown_content.append(format_inline_code())
        elif command == "new-line":
            markdown_content.append(format_new_line())
        elif command == "ordered-list":
            markdown_content.append(format_list(is_ordered=True))
        elif command == "unordered-list":
            markdown_content.append(format_list(is_ordered=False))

        # Виводимо оновлений вміст
        print("\n".join(markdown_content))


if __name__ == "__main__":
    main()
