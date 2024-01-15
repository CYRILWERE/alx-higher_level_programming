#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys

def print_stats(total_size, status_codes):
    """
    Prints the computed statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the count of each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) > 7:
                total_size += int(data[-1])
                code = int(data[-2])
                if code in status_codes:
                    status_codes[code] += 1

            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

