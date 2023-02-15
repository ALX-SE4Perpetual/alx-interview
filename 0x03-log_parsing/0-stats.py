#!/usr/bin/python3

"""
Script that reads stdin line by line and computes metrics
"""

import sys

# Initialize variables
total_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin):
        # Parse line and extract relevant information
        try:
            ip, _, _, date, _, request, status, size = line.split()
            if request != "GET /projects/260 HTTP/1.1":
                continue
            status = int(status)
            size = int(size)
        except ValueError:
            continue

        # Update total file size
        total_size += size

        # Update number of lines by status code
        if status in status_codes:
            status_codes[status] += 1
        else:
            status_codes[status] = 1

        # Print statistics every 10 lines
        if (i + 1) % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes):
                print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    # Handle keyboard interrupt
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")
