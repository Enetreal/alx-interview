#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys

def print_stats(sum_file_size, status_code):
    """Prints the accumulated metrics"""
    print('File size: {:d}'.format(sum_file_size))
    for key in sorted(status_code.keys()):
        if status_code[key] != 0:
            print('{}: {}'.format(key, status_code[key]))

i = 0
sum_file_size = 0
status_code = {'200': 0,
               '301': 0,
               '400': 0,
               '401': 0,
               '403': 0,
               '404': 0,
               '405': 0,
               '500': 0}

try:
    for line in sys.stdin:
        args = line.split()
        if len(args) > 6:
            status_line = args[-2]
            file_size = args[-1]
            if status_line in status_code:
                status_code[status_line] += 1
            try:
                sum_file_size += int(file_size)
            except ValueError:
                pass
            i += 1
            if i == 10:
                print_stats(sum_file_size, status_code)
                i = 0
except KeyboardInterrupt:
    print_stats(sum_file_size, status_code)
    raise
finally:
    print_stats(sum_file_size, status_code)
