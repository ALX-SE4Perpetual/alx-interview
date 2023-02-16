#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import re

regex = (
    r'^([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}) - '
    r'\[(.*)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$'
)

logs = []
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
size = 0
line_count = 0


def print_logs() -> None:
    """Prints logs"""
    global size

    for log in logs:
        size += int(re.match(regex, log).group(4))
        status_code = int(re.match(regex, log).group(3))
        if status_code in status_codes:
            status_codes[status_code] += 1

    print("File size: {}".format(size))
    for key, value in status_codes.items():
        if value > 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    try:
        while True:
            log = input()
            if re.match(regex, log):
                logs.append(log)
                line_count += 1
                if line_count % 10 == 0:
                    print_logs()
                    logs.clear()
                    line_count = 0

            else:
                continue
    except (KeyboardInterrupt, EOFError):
        print_logs()
