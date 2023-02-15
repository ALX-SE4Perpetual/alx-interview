#!/usr/bin/env python3

import sys
from collections import defaultdict

# Initialize counters and variables
total_size = 0
status_counts = defaultdict(int)
line_count = 0

# Read input from stdin
for line in sys.stdin:
    line = line.strip()

    # Parse input line
    try:
        ip, _, _, date, _, request, status, size = line.split()
        method, path, protocol = request.split()
        size = int(size)
        status = int(status)
    except ValueError:
        continue  # Skip line if input format is invalid

    # Update counters and variables
    total_size += size
    status_counts[status] += 1
    line_count += 1

    # Print statistics every 10 lines or on keyboard interrupt (CTRL+C)
    if line_count % 10 == 0:
        print(f'Total file size: {total_size}')

        for code in sorted(status_counts.keys()):
            if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                count = status_counts[code]
                print(f'{code}: {count}')

    try:
        if line_count % 10 == 0:
            sys.stdout.flush()  # Make sure output is flushed to stdout
    except KeyboardInterrupt:
        print(f'Total file size: {total_size}')

        for code in sorted(status_counts.keys()):
            if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                count = status_counts[code]
                print(f'{code}: {count}')

        sys.exit(0)

# Print final statistics
print(f'Total file size: {total_size}')

for code in sorted(status_counts.keys()):
    if code in [200, 301, 400, 401, 403, 404, 405, 500]:
        count = status_counts[code]
        print(f'{code}: {count}')

