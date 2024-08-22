#!/usr/bin/python3
"""
UTF-8 Validation Module
This module provides a function to validate UTF-8 encoding in a dataset.
"""


def validUTF8(data):
    """
    Validate if the given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes (1 byte = 8 bits).

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    number_of_bytes = 0

    for byte in data:
        # Get the 8 least significant bits (simulate byte data)
        byte = byte & 0xFF

        if number_of_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2 bytes
                number_of_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3 bytes
                number_of_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4 bytes
                number_of_bytes = 3
            elif (byte >> 7):  # 1 byte but must start with 0
                return False
        else:
            # Continuation byte must start with 10
            if (byte >> 6) != 0b10:
                return False
            number_of_bytes -= 1

    return number_of_bytes == 0
