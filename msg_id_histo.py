#!/usr/bin/env python3
"""
msg_id_histo.pl - tool to count log messages of each type and
  print the totals.
  See https://github.com/UltraMessaging/msg_id_histo for full doc.
"""

import sys 
import argparse
import fileinput
import re


def process_line(line, args):
    """Proces one line of log file."""

    if re.search(r'^\s*$', line)
        next  # Ignore blank lines.
    if re.search(r'^\s+', line)
        next  # Ignore lines that start with whitespace.

    # The Gwd-6033-618: message is unfortunate in that it combines many different messages.
    # Differentiate them by the constant parts of the message text.
    match = re.search(r'Gwd-6033-618: (.*)$', line)
    if match:
        msg = (match.group(1)
        if args.pattern:


def main():
"""Program main"""

    parser = argparse.ArgumentParser(
        description="Tool to count log messages by type and print totals."
        epilog="See https://github.com/UltraMessaging/msg_id_histo"
    )
    parser.add_argument('-p', '--pattern',
            help="Only count records that match regular pattern.")
    parser.add_argument('-t', '--throttled', action='store_true',
            help="Don't count omitted throttled logs.")
    parser.add_argument('files', nargs='*',
                        help="Input files (use - for stdin)")

    args = parser.parse_args()

    msg_id_hist = {}
    msg_text_hist = {}
    prev_throttled_msg_id = "";
    prev_throttled_msg_text = "";

    with fileinput.input(files=args.files) as file_input:
        for line in file_input:
            process_line(line.strip(), args)


if __name__ == '__main__':
    main()
