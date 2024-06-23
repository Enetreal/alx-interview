#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys

# Initialize cache for status codes and total file size
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

def print_stats(total_size, cache):
    """Prints the accumulated metrics"""
    print('File size: {}'.format(total_size))
    for key in sorted(cache.keys()):
        if cache[key] != 0:
            print('{}: {}'.format(key, cache[key]))

try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) > 6:
            try:
                code = line_list[-2]
                size = int(line_list[-1])
                if code in cache:
                    cache[code] += 1
                total_size += size
                counter += 1
            except ValueError:
                continue

        if counter == 10:
            print_stats(total_size, cache)
            counter = 0

except KeyboardInterrupt:
    print_stats(total_size, cache)
    raise

finally:
    print_stats(total_size, cache)
