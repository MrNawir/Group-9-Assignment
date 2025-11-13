"""
List Questions Solutions
"""


# Question 1: Generate list of first and last 5 square numbers between 1 and 30
def first_last_five_squares():
    """
    Generate and print a list of the first and last 5 elements 
    where the values are square numbers between 1 and 30 (both included).
    
    Returns:
        List containing first 5 and last 5 square numbers
    """
    squares = [i**2 for i in range(1, 31)]
    result = squares[:5] + squares[-5:]
    return result


# Question 2: Calculate difference between two lists
def list_difference(list1, list2):
    """
    Calculate the difference between two lists.
    Returns elements in list1 that are not in list2.
    
    Args:
        list1: First list
        list2: Second list
    
    Returns:
        List of elements in list1 but not in list2
    """
    return [item for item in list1 if item not in list2]


# Question 3: Concatenate list with range from 1 to n
def concatenate_with_range(lst, n):
    """
    Create a list by concatenating a given list with a range from 1 to n.
    
    Sample:
    ['p', 'q'], n=5
    Output: ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
    
    Args:
        lst: Input list
        n: Range limit
    
    Returns:
        Concatenated list
    """
    result = []
    for i in range(1, n + 1):
        for item in lst:
            result.append(f"{item}{i}")
    return result


# Question 4: Convert list to list of dictionaries
def lists_to_dict_list(names, codes):
    """
    Convert two lists to a list of dictionaries.
    
    Sample:
    ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
    Output: [{'color_name': 'Black', 'color_code': '#000000'}, ...]
    
    Args:
        names: List of color names
        codes: List of color codes
    
    Returns:
        List of dictionaries
    """
    return [{'color_name': name, 'color_code': code} 
            for name, code in zip(names, codes)]


# Question 5: Move all zero digits to end
def move_zeros_to_end(lst):
    """
    Move all zero digits to the end of a given list of numbers.
    
    Sample:
    [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    Output: [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    Args:
        lst: Input list
    
    Returns:
        List with all zeros moved to the end
    """
    non_zeros = [x for x in lst if x != 0]
    zeros = [x for x in lst if x == 0]
    return non_zeros + zeros


# Question 6: Round numbers, find min/max, multiply by 5, print unique ascending
def process_numbers(lst):
    """
    Round the numbers in a given list, print the minimum and maximum numbers,
    and multiply the numbers by 5. Print the unique numbers in ascending order.
    
    Sample:
    [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
    Minimum value: 4
    Maximum value: 22
    Result: 20 25 45 55 60 70 80 90 110
    
    Args:
        lst: Input list of numbers
    
    Returns:
        Tuple of (min_value, max_value, result_string)
    """
    # Round the numbers
    rounded = [round(x) for x in lst]
    
    # Find min and max
    min_val = min(rounded)
    max_val = max(rounded)
    
    # Multiply by 5 and get unique values
    multiplied = [x * 5 for x in rounded]
    unique_sorted = sorted(set(multiplied))
    
    # Create result string
    result_str = ' '.join(map(str, unique_sorted))
    
    return min_val, max_val, result_str


# Question 7: Count number of lists in a list of lists
def count_lists(lst):
    """
    Count the number of lists in a given list of lists.
    
    Sample:
    [[1, 3], [5, 7], [9, 11], [13, 15, 17]] -> 4
    [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]] -> 3
    
    Args:
        lst: Input list of lists
    
    Returns:
        Number of lists at the top level
    """
    return len([item for item in lst if isinstance(item, list)])


# Test cases
if __name__ == "__main__":
    print("=" * 60)
    print("Question 1: First and Last 5 Square Numbers")
    print("=" * 60)
    result = first_last_five_squares()
    print(f"First and last 5 square numbers: {result}")
    
    print("\n" + "=" * 60)
    print("Question 2: List Difference")
    print("=" * 60)
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8]
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Difference: {list_difference(list1, list2)}")
    
    print("\n" + "=" * 60)
    print("Question 3: Concatenate with Range")
    print("=" * 60)
    sample_list = ['p', 'q']
    n = 5
    print(f"Sample list: {sample_list}")
    print(f"n = {n}")
    print(f"Sample Output: {concatenate_with_range(sample_list, n)}")
    
    print("\n" + "=" * 60)
    print("Question 4: Convert List to List of Dictionaries")
    print("=" * 60)
    names = ["Black", "Red", "Maroon", "Yellow"]
    codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    result = lists_to_dict_list(names, codes)
    print(f"Expected Output:")
    for item in result:
        print(item)
    
    print("\n" + "=" * 60)
    print("Question 5: Move Zeros to End")
    print("=" * 60)
    original = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    print(f"Original list:\n{original}")
    moved = move_zeros_to_end(original)
    print(f"Move all zero digits to end of the said list of numbers:\n{moved}")
    
    print("\n" + "=" * 60)
    print("Question 6: Process Numbers")
    print("=" * 60)
    original_list = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
    print(f"Original list:\n{original_list}")
    min_val, max_val, result_str = process_numbers(original_list)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
    print(f"Result:\n{result_str}")
    
    print("\n" + "=" * 60)
    print("Question 7: Count Lists")
    print("=" * 60)
    list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
    print(f"Original list:\n{list1}")
    print(f"Number of lists in said list of lists:\n{count_lists(list1)}")
    
    list2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
    print(f"\nOriginal list:\n{list2}")
    print(f"Number of lists in said list of lists:\n{count_lists(list2)}")
