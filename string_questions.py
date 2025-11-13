"""
String Questions Solutions
"""


# Question 1: Get first three characters of a string
def first_three(s):
    """
    Get a string made of the first three characters of a specified string.
    If the length of the string is less than 3, return the original string.
    
    Sample:
    first_three('ipy') -> 'ipy'
    first_three('python') -> 'pyt'
    """
    if len(s) < 3:
        return s
    return s[:3]


# Question 2: Caesar encryption
def caesar_cipher(text, shift):
    """
    Create a Caesar encryption.
    
    In cryptography, a Caesar cipher is one of the simplest encryption techniques.
    Each letter in the plaintext is replaced by a letter some fixed number of 
    positions down the alphabet.
    
    Args:
        text: The text to encrypt
        shift: Number of positions to shift (positive for right shift, negative for left)
    
    Returns:
        Encrypted text
    """
    result = ""
    
    for char in text:
        if char.isupper():
            # Shift uppercase letters
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Shift lowercase letters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep non-alphabetic characters as is
            result += char
    
    return result


# Question 3: Remove duplicate characters from a string
def remove_duplicates(s):
    """
    Remove duplicate characters from a given string.
    
    Args:
        s: Input string
    
    Returns:
        String with duplicates removed (preserving first occurrence order)
    """
    seen = set()
    result = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)


# Question 4: Delete all occurrences of a specified character
def delete_character(s, char_to_delete):
    """
    Delete all occurrences of a specified character in a given string.
    
    Sample:
    Original string: "Delete all occurrences of a specified character in a given string"
    Modified string: "Delete ll occurrences of specified chrcter in given string"
    (when deleting 'a')
    
    Args:
        s: Input string
        char_to_delete: Character to remove
    
    Returns:
        String with all occurrences of the character removed
    """
    return s.replace(char_to_delete, '')


# Question 5: Count leap years within a range
def count_leap_years(year_range):
    """
    Count the number of leap years within the range of years.
    Ranges of years should be accepted as strings.
    
    Sample Data:
    ("1981-1991") -> 2
    ("2000-2020") -> 6
    
    Args:
        year_range: String in format "YYYY-YYYY"
    
    Returns:
        Number of leap years in the range
    """
    start_year, end_year = map(int, year_range.split('-'))
    
    count = 0
    for year in range(start_year, end_year + 1):
        # A leap year is divisible by 4, except for century years
        # Century years must be divisible by 400
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            count += 1
    
    return count


# Question 6: Insert space before every capital letter
def insert_space_before_caps(word):
    """
    Insert space before every capital letter appears in a given word.
    
    Sample Data:
    ("PythonExercises") -> "Python Exercises"
    ("Python") -> "Python"
    ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"
    
    Args:
        word: Input string
    
    Returns:
        String with spaces inserted before capital letters (except first character)
    """
    if not word:
        return word
    
    result = [word[0]]
    
    for char in word[1:]:
        if char.isupper():
            result.append(' ')
        result.append(char)
    
    return ''.join(result)


# Test cases
if __name__ == "__main__":
    print("=" * 60)
    print("Question 1: First Three Characters")
    print("=" * 60)
    print(f"first_three('ipy') -> {first_three('ipy')}")
    print(f"first_three('python') -> {first_three('python')}")
    print(f"first_three('ab') -> {first_three('ab')}")
    
    print("\n" + "=" * 60)
    print("Question 2: Caesar Cipher")
    print("=" * 60)
    print(f"caesar_cipher('HELLO', 3) -> {caesar_cipher('HELLO', 3)}")
    print(f"caesar_cipher('Python', 3) -> {caesar_cipher('Python', 3)}")
    print(f"caesar_cipher('xyz', 3) -> {caesar_cipher('xyz', 3)}")
    
    print("\n" + "=" * 60)
    print("Question 3: Remove Duplicates")
    print("=" * 60)
    test_str = "programming"
    print(f"remove_duplicates('{test_str}') -> {remove_duplicates(test_str)}")
    
    print("\n" + "=" * 60)
    print("Question 4: Delete Character")
    print("=" * 60)
    original = "Delete all occurrences of a specified character in a given string"
    print(f"Original string:\n{original}")
    modified = delete_character(original, 'a')
    print(f"Modified string (deleting 'a'):\n{modified}")
    
    print("\n" + "=" * 60)
    print("Question 5: Count Leap Years")
    print("=" * 60)
    print(f"count_leap_years('1981-1991') -> {count_leap_years('1981-1991')}")
    print(f"count_leap_years('2000-2020') -> {count_leap_years('2000-2020')}")
    
    print("\n" + "=" * 60)
    print("Question 6: Insert Space Before Capitals")
    print("=" * 60)
    print(f"insert_space_before_caps('PythonExercises') -> {insert_space_before_caps('PythonExercises')}")
    print(f"insert_space_before_caps('Python') -> {insert_space_before_caps('Python')}")
    print(f"insert_space_before_caps('PythonExercisesPracticeSolution') -> {insert_space_before_caps('PythonExercisesPracticeSolution')}")
