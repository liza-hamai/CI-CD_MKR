import os

def read_file(file_path):
    """Зчитує рядки з файлу та повертає їх у вигляді множини."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return set()