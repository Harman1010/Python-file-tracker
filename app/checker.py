from pathlib import Path


def check_python_file(file_path: str) -> dict:
    """Check whether a Python file exists and is not empty."""
    path = Path(file_path)

    if not path.exists():
        return {
            "valid": False,
            "message": f"File not found: {file_path}",
        }

    if not path.is_file():
        return {
            "valid": False,
            "message": f"Not a file: {file_path}",
        }

    if path.suffix != ".py":
        return {
            "valid": False,
            "message": f"Not a Python file: {file_path}",
        }

    if path.stat().st_size == 0:
        return {
            "valid": False,
            "message": f"File is empty: {file_path}",
        }

    return {
        "valid": True,
        "message": f"Python file looks good: {file_path}",
    }
