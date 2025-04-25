"""
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
"""

import sys
import argparse
from ProductionCode.most_banned import (
    most_banned_districts,
    most_banned_authors,
    most_banned_states,
    most_banned_titles,
)


def main():
    """Main function for the command line interface (CLI) for the project."""
    parser = argparse.ArgumentParser(
        # The command line interface (CLI) for the project.
        prog="cl.py",
        description="Command line interface for the project",
        epilog="This is the command line interface for the project.",
        usage="%(prog)s [options] [args]",
    )
    parser.add_argument(
        # Get the most banned districts in the database
        "--most-banned-districts",
        "--mbd",
        "-mbd",
        help="Get the most banned districts in the database",
        type=int,
        metavar="LIMIT",
    )
    parser.add_argument(
        # Get the most banned authors in the database
        "--most-banned-authors",
        "--mba",
        "-mba",
        help="Get the most banned authors in the database",
        type=int,
        metavar="LIMIT",
    )
    parser.add_argument(
        # Get the most banned states in the database
        "--most-banned-states",
        "--mbs",
        "-mbs",
        help="Get the most banned states in the database",
        type=int,
        metavar="LIMIT",
    )
    parser.add_argument(
        # Get the most banned titles in the database
        "--most-banned-titles",
        "--mbt",
        "-mbt",
        help="Get the most banned titles in the database",
        type=int,
        metavar="LIMIT",
    )
    args = parser.parse_args()
    dispatch = {
        "most_banned_districts": most_banned_districts,
        "most_banned_authors": most_banned_authors,
        "most_banned_states": most_banned_states,
        "most_banned_titles": most_banned_titles,
    }
    for attr, func in dispatch.items():
        if getattr(args, attr) is not None:
            search_results = func(getattr(args, attr))
            for result in search_results:
                print(result)
            break
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
