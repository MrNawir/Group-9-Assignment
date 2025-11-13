"""
Tuple Questions Solutions
"""


# Question 1: Replace last value of tuples in a list
def replace_last_value(tuple_list, new_value=100):
    """
    Replace the last value of tuples in a list.
    
    Sample:
    [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
    
    Args:
        tuple_list: List of tuples
        new_value: Value to replace the last element with (default: 100)
    
    Returns:
        List of tuples with last values replaced
    """
    return [t[:-1] + (new_value,) for t in tuple_list]


# Question 2: Remove empty tuples from list
def remove_empty_tuples(tuple_list):
    """
    Remove empty tuple(s) from a list of tuples.
    
    Sample:
    [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
    
    Note: This keeps tuples with empty strings but removes completely empty tuples
    
    Args:
        tuple_list: List of tuples
    
    Returns:
        List with empty tuples removed
    """
    return [t for t in tuple_list if t != ()]


# Question 3: Sort tuple by float element
def sort_by_float(tuple_list):
    """
    Sort a tuple by its float element.
    
    Sample:
    [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
    
    Args:
        tuple_list: List of tuples with string float values
    
    Returns:
        List sorted by float values in descending order
    """
    return sorted(tuple_list, key=lambda x: float(x[1]), reverse=True)


# Question 4: Convert tuple of positive integers to integer
def tuple_to_int(t):
    """
    Convert a given tuple of positive integers into an integer.
    
    Sample:
    (1, 2, 3) -> 123
    (10, 20, 40, 5, 70) -> 102040570
    
    Args:
        t: Tuple of positive integers
    
    Returns:
        Integer formed by concatenating tuple elements
    """
    return int(''.join(map(str, t)))


# Question 5: Sum of elements in each tuple
def sum_tuples(tuple_list):
    """
    Compute the sum of all the elements of each tuple stored inside a list of tuples.
    
    Sample:
    [(1, 2), (2, 3), (3, 4)] -> [3, 5, 7]
    [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)] -> [9, -1, 7, 8]
    
    Args:
        tuple_list: List of tuples
    
    Returns:
        List of sums
    """
    return [sum(t) for t in tuple_list]


# Question 6: Average value of numbers in tuple of tuples
def average_tuple_of_tuples(tuple_of_tuples):
    """
    Calculate the average value of the numbers in a given tuple of tuples.
    
    Sample:
    ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
    Average: [30.5, 34.25, 27.0, 23.25]
    
    Args:
        tuple_of_tuples: Tuple of tuples with numbers
    
    Returns:
        List of average values for each position
    """
    if not tuple_of_tuples or not tuple_of_tuples[0]:
        return []
    
    num_positions = len(tuple_of_tuples[0])
    averages = []
    
    for i in range(num_positions):
        # Get all values at position i from all tuples
        values = [t[i] for t in tuple_of_tuples if len(t) > i]
        avg = sum(values) / len(values)
        averages.append(avg)
    
    return averages


# Test cases
if __name__ == "__main__":
    print("=" * 60)
    print("Question 1: Replace Last Value of Tuples")
    print("=" * 60)
    sample = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    print(f"Sample list: {sample}")
    result = replace_last_value(sample)
    print(f"Expected Output: {result}")
    
    print("\n" + "=" * 60)
    print("Question 2: Remove Empty Tuples")
    print("=" * 60)
    sample = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    print(f"Sample data: {sample}")
    result = remove_empty_tuples(sample)
    print(f"Expected output: {result}")
    
    print("\n" + "=" * 60)
    print("Question 3: Sort Tuple by Float Element")
    print("=" * 60)
    sample = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    print(f"Sample data: {sample}")
    result = sort_by_float(sample)
    print(f"Expected Output: {result}")
    
    print("\n" + "=" * 60)
    print("Question 4: Convert Tuple to Integer")
    print("=" * 60)
    tuple1 = (1, 2, 3)
    print(f"Original tuple:\n{tuple1}")
    print(f"Convert the said tuple of positive integers into an integer:\n{tuple_to_int(tuple1)}")
    
    tuple2 = (10, 20, 40, 5, 70)
    print(f"\nOriginal tuple:\n{tuple2}")
    print(f"Convert the said tuple of positive integers into an integer:\n{tuple_to_int(tuple2)}")
    
    print("\n" + "=" * 60)
    print("Question 5: Sum of Elements in Each Tuple")
    print("=" * 60)
    list1 = [(1, 2), (2, 3), (3, 4)]
    print(f"Original list of tuples:\n{list1}")
    result = sum_tuples(list1)
    print(f"Sum of all the elements of each tuple stored inside the said list of tuples:\n{result}")
    
    list2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
    print(f"\nOriginal list of tuples:\n{list2}")
    result = sum_tuples(list2)
    print(f"Sum of all the elements of each tuple stored inside the said list of tuples:\n{result}")
    
    print("\n" + "=" * 60)
    print("Question 6: Average Value in Tuple of Tuples")
    print("=" * 60)
    tuple1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
    print(f"Original Tuple:\n{tuple1}")
    result = average_tuple_of_tuples(tuple1)
    print(f"Average value of the numbers of the said tuple of tuples:\n{result}")
    
    tuple2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
    print(f"\nOriginal Tuple:\n{tuple2}")
    result = average_tuple_of_tuples(tuple2)
    print(f"Average value of the numbers of the said tuple of tuples:\n{result}")
