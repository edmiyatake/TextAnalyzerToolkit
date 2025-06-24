import sys

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

def basic_analysis(text):
    lines = text.split('\n')
    words = text.split()
    characters = len(text)
    return {
        'lines': len(lines),
        'words': len(words),
        'characters': characters
    }

def print_report(stats):
    print("Text Analysis Report")
    print(f"Lines     : {stats['lines']}")
    print(f"Words     : {stats['words']}")
    print(f"Characters: {stats['characters']}")

# GOAL: read in text file and create stats

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    filepath = sys.argv[1]
    content = read_file(filepath)

    if content:
        stats = basic_analysis(content)
        print_report(stats)
