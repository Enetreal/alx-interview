#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys
from collections import defaultdict

total_file_size = 0
status_codes = defaultdict(int)

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            ip_address, date, request, status_code, file_size = line.strip().split(" - ", 1)[0].split(" - ")
            status_code = int(status_code.split(" ")[1])
            file_size = int(file_size)
            status_codes[status_code] += 1
            total_file_size += file_size
        except (ValueError, IndexError):
            continue

        if i % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")