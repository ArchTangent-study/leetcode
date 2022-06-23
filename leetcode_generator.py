# Generates a folder for given leetcode number (LCXXX) and name.
# 
# What's generated:
# - Folder
# - README.md
# - ${NUM}_${name_of_project}_1.py
#
# Usage: 
# In desired folder, type `python {path to leetcode_generator.py}`
# - example: `python ../leetcode_generator.py`
from pathlib import Path

def to_snake_case(string: str):
    """Returns input string in snake_case."""
    return string.lower().strip().replace(' ', '_')


def generate_py_filename(name: str, number: int) -> str:
    """Returns Python filename for the problem."""
    text = to_snake_case(name)
    return f"{number:03}_{text}_1.py"


def generate_py_file_data() -> str:
    """Returns string data that will be in Python file for the problem."""
    py_file = """#type: ignore"""
    return py_file


def generate_readme(name: str, number: int, diff: str) -> str:
    """Returns string representation of data for LC template README."""
    body = """
## Problem


## Thought Process

Edge Cases / Caveats / Pitfalls:

## Procedure

### Method 1

## Results (Python 3)

**Method 1**:  ms, MB (%, %)
"""
    difficulty = diff.title()
    header = f"# {name} ([LC{number:03}]())\nDifficulty: {difficulty}"

    return f"{header}\n{body}"


def cli():
    """Entry point for the program."""
    cwd = Path.cwd()

    input_number = int(input("Input LeetCode Number: "))
    input_name = input("Input LeetCode Name: ")
    input_diff = input("Input Difficulty: ")

    pyfile_data = generate_py_file_data()
    readme_data = generate_readme(input_name, input_number, input_diff)
    pyfilename = generate_py_filename(input_name, input_number)
    foldername = to_snake_case(input_name)

    folder_path = cwd / foldername
    readme_path = folder_path / "README.md"
    pyfile_path = folder_path / pyfilename

    # Note: Path.mkdir() will error by default if folder/file already exist.
    print(f"\nCreating folder '{folder_path}'...")
    try:
        folder_path.mkdir()
    except FileExistsError:
        print("...folder already exists!")
    except FileNotFoundError:
        raise FileNotFoundError(f"parent folder '{foldername}' not found!")

    print(f"Creating '{pyfilename}'...")
    if not pyfile_path.exists():
        with open(pyfile_path,"w") as file:
            file.write(pyfile_data)
    else:
        print(f"...'{pyfilename}' already exists!")

    print(f"Creating 'README.md'...")
    if not readme_path.exists():
        with open(readme_path,"w") as file:
            file.write(readme_data)
    else:
        print(f"...'README.md' already exists!")
    
    print("...done!\n")

if __name__ == "__main__":
    print("\n----- LeetCode Project Generator -----\n")
    cli()
