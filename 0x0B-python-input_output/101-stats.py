#!/usr/bin/python3
"""Reads from standard input, processes log entries, and computes metrics.
"""

def print_stats(size, status_codes):
    """Print accumulated metrics.
    Args:
        size (int): Total file size.
        status_codes (dict): Dictionary containing HTTP status code counts.
    """
    print("Total File Size: {}".format(size))
    for code, count in sorted(status_codes.items()):
        print("HTTP {}: {}".format(code, count))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            elements = line.split()

            try:
                size += int(elements[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = elements[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

