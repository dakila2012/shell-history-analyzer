import os
import sys
from collections import Counter
def load_history(file_path=None):
    if file_path is None:
        file_path = os.path.expanduser("~/.bash_history")
    else:
        file_path = os.path.expanduser(file_path)
    commands = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped:
                    commands.append(stripped)
        if not commands:
            print(f"History file '{file_path}' is empty.", file=sys.stderr)
            return []
    except FileNotFoundError:
        print(f"Error: History file '{file_path}' not found.", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}", file=sys.stderr)
        return []
    return commands
def count_frequencies(commands):
    return Counter(commands)
def get_top_commands(counter, n=10):
    if n is None or n <= 0:
        return counter.most_common()
    return counter.most_common(n)
def search_commands(commands, term):
    term_lower = term.lower()
    return [cmd for cmd in commands if term_lower in cmd.lower()]
