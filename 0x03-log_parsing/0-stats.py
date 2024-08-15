#!/usr/bin/python3
import sys
import signal

# Global variables
total_file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0


def print_stats():
    """Prints the statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles keyboard interruption"""
    print_stats()
    sys.exit(0)


# Register signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        try:
            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]

            # Update total file size
            total_file_size += file_size

            # Update status code count
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            continue

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Print final statistics if script ends naturally
print_stats()
