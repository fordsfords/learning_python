#!/usr/bin/env python3
"""
msg_id_histo.pl - tool to count log messages of each type and
  print the totals.
  See https://github.com/UltraMessaging/msg_id_histo for full doc.
"""

import re


# Emulate Perl's 'while (<>) {' diamond operator.


def main():
    msg_id_hist = {}
    msg_text_hist = {}
    prev_throttled_msg_id = "";
    prev_throttled_msg_text = "";

    for line in fileinput.input():
        if re.search(r'^\s*$', line)
            next  # Ignore blank lines.
        if re.search(r'^\s+', line)
            next  # Ignore lines that start with whitespace.


# This code only runs when the file is executed directly.
if __name__ == '__main__':
    main()
