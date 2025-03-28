import pytest
import os
from main import read_file, compare_files, write_to_file, main


@pytest.fixture
def sample_files(tmp_path):
    """Створює тимчасові файли для тестування."""
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    same_file = tmp_path / "same.txt"
    diff_file = tmp_path / "diff.txt"

    file1.write_text("apple\nbanana\ncherry\n")
    file2.write_text("banana\ncherry\ndate\n")

    return file1, file2, same_file, diff_file


@pytest.mark.parametrize("content, expected", [
    ("apple\nbanana\ncherry\n", {"apple", "banana", "cherry"}),
    ("banana\ncherry\ndate\n", {"banana", "cherry", "date"}),
    ("", set()),
])
def test_read_file(tmp_path, content, expected):
    """Тестуємо функцію read_file."""
    test_file = tmp_path / "test.txt"
    test_file.write_text(content)
    assert read_file(test_file) == expected


def test_compare_files(sample_files):
    """Тестуємо функцію compare_files."""
    file1, file2, _, _ = sample_files
    common, different = compare_files(file1, file2)
    assert common == {"banana", "cherry"}
    assert different == {"apple", "date"}


def test_write_to_file(sample_files):
    """Тестуємо функцію write_to_file."""
    _, _, same_file, _ = sample_files
    lines = {"banana", "cherry"}
    write_to_file(same_file, lines)
    assert same_file.read_text().strip().split("\n") == sorted(lines)


