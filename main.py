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