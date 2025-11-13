"""
Dictionary Questions Solutions
"""

from collections import Counter


# Question 1: Concatenate dictionaries
def concatenate_dicts(*dicts):
    """
    Concatenate multiple dictionaries to create a new one.
    
    Sample:
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}
    Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    
    Args:
        *dicts: Variable number of dictionaries
    
    Returns:
        Concatenated dictionary
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result


# Question 2: Print all distinct values in a dictionary
def distinct_values(dict_list):
    """
    Print all distinct values in a dictionary.
    
    Sample Data:
    [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
     {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    
    Expected Output:
    Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
    
    Args:
        dict_list: List of dictionaries
    
    Returns:
        Set of unique values
    """
    values = set()
    for d in dict_list:
        values.update(d.values())
    return values


# Question 3: Combine two dictionaries by adding values for common keys
def combine_dicts_with_counter(d1, d2):
    """
    Combine two dictionaries by adding values for common keys using Counter.
    
    Sample:
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    Output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
    
    Args:
        d1: First dictionary
        d2: Second dictionary
    
    Returns:
        Counter object with combined values
    """
    counter1 = Counter(d1)
    counter2 = Counter(d2)
    return counter1 + counter2


# Question 4: Get top three items in a shop
def top_three_items(items):
    """
    Get the top three items in a shop by value.
    
    Sample data:
    {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
    
    Expected Output:
    item4 55
    item1 45.5
    item3 41.3
    
    Args:
        items: Dictionary of items with their values
    
    Returns:
        List of tuples (item_name, value) for top 3 items
    """
    # Sort by value in descending order and get top 3
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:3]


# Question 5: Filter dictionary based on values
def filter_dict_by_value(d, threshold):
    """
    Filter a dictionary based on values.
    
    Sample:
    Original Dictionary:
    {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    Marks greater than 170:
    {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
    
    Args:
        d: Input dictionary
        threshold: Minimum value threshold
    
    Returns:
        Filtered dictionary
    """
    return {k: v for k, v in d.items() if v > threshold}


# Question 6: Extract list of values from list of dictionaries
def extract_values_by_key(dict_list, key):
    """
    Extract a list of values from a given list of dictionaries.
    
    Sample:
    Original Dictionary:
    [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
    Extract where subject = Science -> [92, 94, 88]
    
    Args:
        dict_list: List of dictionaries
        key: Key to extract values for
    
    Returns:
        List of values
    """
    return [d[key] for d in dict_list if key in d]


# Test cases
if __name__ == "__main__":
    print("=" * 60)
    print("Question 1: Concatenate Dictionaries")
    print("=" * 60)
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    result = concatenate_dicts(dic1, dic2, dic3)
    print(f"dic1 = {dic1}")
    print(f"dic2 = {dic2}")
    print(f"dic3 = {dic3}")
    print(f"Expected Result: {result}")
    
    print("\n" + "=" * 60)
    print("Question 2: Distinct Values")
    print("=" * 60)
    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
                   {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, 
                   {"VIII": "S007"}]
    print(f"Sample Data:\n{sample_data}")
    unique = distinct_values(sample_data)
    print(f"Unique Values: {unique}")
    
    print("\n" + "=" * 60)
    print("Question 3: Combine Dictionaries with Counter")
    print("=" * 60)
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    print(f"d1 = {d1}")
    print(f"d2 = {d2}")
    result = combine_dicts_with_counter(d1, d2)
    print(f"Sample output:\n{result}")
    
    print("\n" + "=" * 60)
    print("Question 4: Top Three Items")
    print("=" * 60)
    items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
    print(f"Sample data:\n{items}")
    print("\nExpected Output:")
    top_items = top_three_items(items)
    for item, value in top_items:
        print(f"{item} {value}")
    
    print("\n" + "=" * 60)
    print("Question 5: Filter Dictionary by Value")
    print("=" * 60)
    original = {'Cierra Vega': 175, 'Alden Cantrell': 180, 
                'Kierra Gentry': 165, 'Pierre Cox': 190}
    print(f"Original Dictionary:\n{original}")
    filtered = filter_dict_by_value(original, 170)
    print(f"Marks greater than 170:\n{filtered}")
    
    print("\n" + "=" * 60)
    print("Question 6: Extract Values by Key")
    print("=" * 60)
    dict_list = [{'Math': 90, 'Science': 92}, 
                 {'Math': 89, 'Science': 94}, 
                 {'Math': 92, 'Science': 88}]
    print(f"Original Dictionary:\n{dict_list}")
    
    science_values = extract_values_by_key(dict_list, 'Science')
    print(f"Extract a list of values from said list of dictionaries where subject = Science")
    print(science_values)
    
    math_values = extract_values_by_key(dict_list, 'Math')
    print(f"\nOriginal Dictionary:\n{dict_list}")
    print(f"Extract a list of values from said list of dictionaries where subject = Math")
    print(math_values)
