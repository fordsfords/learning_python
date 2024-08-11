#!/usr/bin/env python3
"""
Simple example showing a python version of the perl program:
while (<>) {
  if (/echo (.*)/) {
    print "$1\n";
  }
}
"""

import fileinput
import re

# Emulate Perl's 'while (<>) {' diamond operator.
for line in fileinput.input():
    match = re.search(r'^echo (.*)', line)
    if match:
        print(match.group(1))
