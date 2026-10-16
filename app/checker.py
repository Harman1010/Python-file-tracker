from pathlib import Path
import argparse
import sys


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


def main() -> None:
    """Run the checker from the command line."""
    parser = argparse.ArgumentParser(
        description="Check whether a Python file exists and is not empty."
    )
    parser.add_argument(
        "file_path",
        help="Path to the Python file to check",
    )

    args = parser.parse_args()
    result = check_python_file(args.file_path)
    print(result["message"])

    if not result["valid"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
