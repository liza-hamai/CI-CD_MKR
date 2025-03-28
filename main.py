import os


def read_file(file_path):
    """Зчитує рядки з файлу та повертає їх у вигляді множини."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return set()


def compare_files(file1, file2):
    """Порівнює вміст двох файлів і повертає спільні та унікальні рядки."""
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    common_lines = lines1 & lines2
    different_lines = (lines1 | lines2) - common_lines

    return common_lines, different_lines


def write_to_file(file_path, lines):
    """Записує рядки у файл."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in sorted(lines):
            file.write(line + '\n')


def main():
    """Основна функція для порівняння файлів та запису результатів."""
    file1 = 'random_text_1.txt'
    file2 = 'random_text_2.txt'
    same_file = 'same.txt'
    diff_file = 'diff.txt'

    common, different = compare_files(file1, file2)

    write_to_file(same_file, common)
    write_to_file(diff_file, different)

    print(f"Результати збережено у {same_file} та {diff_file}.")

if __name__ == "__main__":
    main()
