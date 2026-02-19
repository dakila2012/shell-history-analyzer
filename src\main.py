import argparse
import sys
from analyzer import (
    load_history,
    count_frequencies,
    get_top_commands,
    search_commands,
)
def main():
    parser = argparse.ArgumentParser(
        prog="shell-history-analyzer",
        description="CLI tool for analyzing shell history files with command frequency counts, top commands, and search using modular src package.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0",
    )
    parser.add_argument(
        "history_file",
        nargs="?",
        default=None,
        help="Path to shell history file (default: ~/.bash_history)",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--top",
        type=int,
        nargs="?",
        const=10,
        metavar="N",
        help="Display the top N most frequent commands (default N=10)",
    )
    group.add_argument(
        "--search",
        "-s",
        help="Search for commands containing the given term (reads from file or stdin)",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Display all commands sorted by frequency.",
    )
    args = parser.parse_args()
    if args.search:
        term = args.search
        if args.history_file:
            commands = load_history(args.history_file)
        else:
            commands = [line.strip() for line in sys.stdin.readlines() if line.strip()]
        if not commands:
            if not args.history_file:
                print("No commands provided via stdin.", file=sys.stderr)
            sys.exit(1)
        matches = search_commands(commands, term)
        if matches:
            print(f"Found {len(matches)} matching commands:")
            for cmd in matches:
                print(cmd)
        else:
            print("No matching commands found.")
    else:
        commands = load_history(args.history_file)
        if not commands:
            sys.exit(1)
        counter = count_frequencies(commands)
        total = len(commands)
        unique = len(counter)
        print(f"Total commands analyzed: {total}")
        print(f"Unique commands: {unique}")
        if args.all:
            n = None
        elif args.top is not None:
            n = args.top
        else:
            n = 10
        top_n = get_top_commands(counter, n)
        for cmd, count in top_n:
            print(f"{cmd}: {count}")
if __name__ == "__main__":
    main()
