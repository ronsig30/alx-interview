# UTF-8 Validation Project

## Project Overview

This project involves implementing a Python function that validates whether a given dataset represents a valid UTF-8 encoding. The validation function, `validUTF8`, examines each byte in the dataset to ensure it adheres to the UTF-8 encoding scheme.

## Files

- `0-validate_utf8.py`: Contains the `validUTF8` function which performs the UTF-8 validation.
- `0-main.py`: A test file to demonstrate the functionality of the `validUTF8` method.
- `README.md`: This file, providing an overview and explanation of the project.

## Function Details

### `validUTF8(data)`

This function validates if the provided dataset is a valid UTF-8 encoding. The dataset is represented as a list of integers, where each integer corresponds to a byte (8 bits).

#### Parameters:
- `data` (list of int): A list of integers representing bytes. Each integer should be in the range 0-255.

#### Returns:
- `bool`: Returns `True` if the data represents a valid UTF-8 encoding, otherwise `False`.

#### Example Usage:
```python
data = [65]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False

