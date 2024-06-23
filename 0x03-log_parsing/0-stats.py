#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys

# Initialize variables
total_size = 0
counter = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

def print_stats():
    """Prints the accumulated metrics."""
    print('File size: {}'.format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print('{}: {}'.format(key, status_codes[key]))

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 6:
            try:
                # Extract the status code and file size
                status_code = parts[-2]
                file_size = int(parts[-1])

                # Update total file size
                total_size += file_size

                # Update status code count
                if status_code in status_codes:
                    status_codes[status_code] += 1

                # Increment line counter
                counter += 1

                # Print stats after every 10 lines
                if counter == 10:
                    print_stats()
                    counter = 0

            except ValueError:
                # Ignore lines with invalid file size
                pass

except KeyboardInterrupt:
    # Handle the keyboard interrupt and print stats
    print_stats()
    raise

finally:
    # Ensure stats are printed when the program ends
    print_stats()
