from app.checker import check_python_file


def test_valid_python_file():
    result = check_python_file("app/checker.py")
    assert result["valid"] is True


def test_missing_file():
    result = check_python_file("missing.py")
    assert result["valid"] is False
    assert "File not found" in result["message"]


def test_empty_file(tmp_path):
    empty_file = tmp_path / "empty.py"
    empty_file.touch()

    result = check_python_file(str(empty_file))

    assert result["valid"] is False
    assert "File is empty" in result["message"]


def test_wrong_extension(tmp_path):
    text_file = tmp_path / "notes.txt"
    text_file.write_text("some content")

    result = check_python_file(str(text_file))

    assert result["valid"] is False
    assert "Not a Python file" in result["message"]


import subprocess
import sys


def test_cli_valid_file():
    result = subprocess.run(
        [sys.executable, "-m", "app.checker", "app/checker.py"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Python file looks good" in result.stdout


def test_cli_missing_file():
    result = subprocess.run(
        [sys.executable, "-m", "app.checker", "missing.py"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "File not found" in result.stdout
