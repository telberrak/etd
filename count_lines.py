import sys

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for _ in file)
            print(f"Total lines: {line_count}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_lines.py <filename>")
    else:
        count_lines(sys.argv[1])
