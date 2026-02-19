shell-history-analyzer

A production-ready CLI tool for analyzing shell history files, such as `~/.bash_history`. It provides command frequency counts, displays top N or all commands sorted by frequency, and supports searching for commands containing a specific term from either a file or stdin. Handles edge cases like missing or empty files gracefully with clear error messages and user-friendly output.

Built as a modular Python package under `src/`, using only the standard library for lightweight, dependency-free operation.

## Installation

No external dependencies required (uses Python standard library only).

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shell-history-analyzer.git
   cd shell-history-analyzer
   ```

2. Run directly:
   ```bash
   python src/main.py --help
   ```

## Usage

```bash
# Show help and usage
python src/main.py --help

# Analyze default bash history (~/.bash_history) - shows top 10 commands with stats
python src/main.py

# Top 10 commands from specific file
python src/main.py ~/.bash_history --top 10

# Top 10 from file (positional arg)
python src/main.py ~/.bash_history --top 10

# All commands sorted by frequency
python src/main.py ~/.bash_history --all

# Search for commands containing "git" from stdin
echo -e "ls\ncd\ngit status\ngit commit\nls" | python src/main.py --search git

# Search in file
python src/main.py ~/.bash_history --search git
```

## Features

- Loads shell history from `~/.bash_history` (default) or specified file
- Displays total commands, unique commands, and frequency counts
- Top N most frequent commands (default N=10)
- All commands sorted by frequency (`--all`)
- Search for commands matching a term (`--search`), from file or stdin
- `--version` support
- Graceful handling of missing/empty files and invalid inputs

## Dependencies

Python standard library only:
- `argparse`
- `os`
- `sys`
- `collections.Counter`

## Tests

No tests implemented.

## License

MIT