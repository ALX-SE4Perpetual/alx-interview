#!/usr/bin/env python3

import sys

# initialize counters
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        # parse the line
        try:
            ip_address, _, _, _, status_code_str, file_size_str = line.split()
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except ValueError:
            # skip line if format is not as expected
            continue

        # update counters
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        # print metrics every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                if status_code_counts[code] > 0:
                    print(f"{code}: {status_code_counts[code]}")
except KeyboardInterrupt:
    # print final metrics on keyboard interrupt
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
