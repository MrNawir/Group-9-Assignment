# Group 9 Assignment - Python Data Structures

This project contains solutions to various Python programming questions organized by data structure types.

## Project Structure

```
Group_9_Assignment/
├── string_questions.py      # Solutions for string manipulation problems
├── list_questions.py         # Solutions for list operations
├── dictionary_questions.py   # Solutions for dictionary operations
├── tuple_questions.py        # Solutions for tuple operations
├── sets_questions.py         # Solutions for set operations
└── README.md                 # This file
```

## Files Overview

### 1. string_questions.py
Contains 6 functions solving string manipulation problems:
- `first_three()` - Get first three characters of a string
- `caesar_cipher()` - Implement Caesar encryption
- `remove_duplicates()` - Remove duplicate characters
- `delete_character()` - Delete all occurrences of a character
- `count_leap_years()` - Count leap years in a date range
- `insert_space_before_caps()` - Insert spaces before capital letters

### 2. list_questions.py
Contains 7 functions solving list operation problems:
- `first_last_five_squares()` - Generate square numbers
- `list_difference()` - Calculate difference between lists
- `concatenate_with_range()` - Concatenate list with range
- `lists_to_dict_list()` - Convert lists to list of dictionaries
- `move_zeros_to_end()` - Move all zeros to end
- `process_numbers()` - Round, find min/max, multiply, and sort
- `count_lists()` - Count number of lists in a list

### 3. dictionary_questions.py
Contains 6 functions solving dictionary operation problems:
- `concatenate_dicts()` - Concatenate multiple dictionaries
- `distinct_values()` - Extract all distinct values
- `combine_dicts_with_counter()` - Combine dictionaries using Counter
- `top_three_items()` - Get top three items by value
- `filter_dict_by_value()` - Filter dictionary based on values
- `extract_values_by_key()` - Extract values from list of dictionaries

### 4. tuple_questions.py
Contains 6 functions solving tuple operation problems:
- `replace_last_value()` - Replace last value in tuples
- `remove_empty_tuples()` - Remove empty tuples from list
- `sort_by_float()` - Sort tuples by float element
- `tuple_to_int()` - Convert tuple of integers to single integer
- `sum_tuples()` - Sum elements in each tuple
- `average_tuple_of_tuples()` - Calculate average values

### 5. sets_questions.py
Contains 7 functions solving set operation problems:
- `set_length()` - Find length of a set
- `add_to_set()` - Add members to a set
- `remove_from_set()` - Remove items from a set
- `set_intersection()` - Create intersection of sets
- `set_union()` - Create union of sets
- `set_difference()` - Create set difference
- `set_min_max()` - Find minimum and maximum values

## How to Run

Each file can be run independently to see test cases and examples:

```bash
# Run string questions
python3 string_questions.py

# Run list questions
python3 list_questions.py

# Run dictionary questions
python3 dictionary_questions.py

# Run tuple questions
python3 tuple_questions.py

# Run sets questions
python3 sets_questions.py
```

## Usage Examples

### Import and use functions:

```python
# Example: Using string functions
from string_questions import first_three, caesar_cipher

result = first_three("python")
print(result)  # Output: "pyt"

encrypted = caesar_cipher("HELLO", 3)
print(encrypted)  # Output: "KHOOR"
```

```python
# Example: Using list functions
from list_questions import move_zeros_to_end

numbers = [3, 0, 4, 0, 5]
result = move_zeros_to_end(numbers)
print(result)  # Output: [3, 4, 5, 0, 0]
```

```python
# Example: Using dictionary functions
from dictionary_questions import concatenate_dicts

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
result = concatenate_dicts(dic1, dic2)
print(result)  # Output: {1: 10, 2: 20, 3: 30, 4: 40}
```

## Features

- All functions include docstrings with descriptions and examples
- Each file includes comprehensive test cases
- Clear output formatting for easy verification
- Follows Python best practices and conventions
- Well-commented and easy to understand

## Notes

- All functions are fully documented with docstrings
- Test cases are included at the bottom of each file
- Functions can be imported and used in other Python scripts
- The code follows PEP 8 style guidelines

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Group Members

Add your group member names here:
- Member 1: Ibrahim Abdu
- Member 2: Ayman Abdi
- Member 3: Abigael Seenoip
- Member 4: Peace Kuria
- Member 5: Emmanuel Hongo
- Member 6: Fredrick Rangara
---

**Assignment completed on:** 14/11/2025
