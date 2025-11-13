"""
Sets Questions Solutions
"""


# Question 1: Find the length of a set
def set_length(s):
    """
    Find the length of a set.
    
    Args:
        s: Input set
    
    Returns:
        Length of the set
    """
    return len(s)


# Question 2: Add member(s) to a set
def add_to_set(s, *items):
    """
    Add member(s) to a set.
    
    Args:
        s: Input set
        *items: Variable number of items to add
    
    Returns:
        Updated set
    """
    for item in items:
        s.add(item)
    return s


# Question 3: Remove item(s) from a given set
def remove_from_set(s, *items):
    """
    Remove item(s) from a given set.
    
    Args:
        s: Input set
        *items: Variable number of items to remove
    
    Returns:
        Updated set
    """
    for item in items:
        s.discard(item)  # Using discard to avoid KeyError if item doesn't exist
    return s


# Question 4: Create an intersection of sets
def set_intersection(set1, set2):
    """
    Create an intersection of sets.
    Returns elements common to both sets.
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Intersection of the two sets
    """
    return set1.intersection(set2)
    # Alternative: return set1 & set2


# Question 5: Create a union of sets
def set_union(set1, set2):
    """
    Create a union of sets.
    Returns all elements from both sets (without duplicates).
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Union of the two sets
    """
    return set1.union(set2)
    # Alternative: return set1 | set2


# Question 6: Create set difference
def set_difference(set1, set2):
    """
    Create set difference.
    Returns elements in set1 that are not in set2.
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Difference (set1 - set2)
    """
    return set1.difference(set2)
    # Alternative: return set1 - set2


# Question 7: Find maximum and minimum values in a set
def set_min_max(s):
    """
    Find the maximum and minimum values in a set.
    
    Args:
        s: Input set
    
    Returns:
        Tuple of (min_value, max_value)
    """
    return (min(s), max(s))


# Test cases
if __name__ == "__main__":
    print("=" * 60)
    print("Question 1: Find Length of a Set")
    print("=" * 60)
    sample_set = {1, 2, 3, 4, 5}
    print(f"Set: {sample_set}")
    print(f"Length: {set_length(sample_set)}")
    
    print("\n" + "=" * 60)
    print("Question 2: Add Members to a Set")
    print("=" * 60)
    sample_set = {1, 2, 3}
    print(f"Original set: {sample_set}")
    result = add_to_set(sample_set, 4, 5, 6)
    print(f"After adding 4, 5, 6: {result}")
    
    print("\n" + "=" * 60)
    print("Question 3: Remove Items from a Set")
    print("=" * 60)
    sample_set = {1, 2, 3, 4, 5, 6}
    print(f"Original set: {sample_set}")
    result = remove_from_set(sample_set, 3, 5)
    print(f"After removing 3, 5: {result}")
    
    print("\n" + "=" * 60)
    print("Question 4: Intersection of Sets")
    print("=" * 60)
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Intersection: {set_intersection(set1, set2)}")
    
    print("\n" + "=" * 60)
    print("Question 5: Union of Sets")
    print("=" * 60)
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {set_union(set1, set2)}")
    
    print("\n" + "=" * 60)
    print("Question 6: Set Difference")
    print("=" * 60)
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Difference (Set1 - Set2): {set_difference(set1, set2)}")
    print(f"Difference (Set2 - Set1): {set_difference(set2, set1)}")
    
    print("\n" + "=" * 60)
    print("Question 7: Maximum and Minimum Values")
    print("=" * 60)
    sample_set = {10, 25, 5, 42, 18, 3, 99}
    print(f"Set: {sample_set}")
    min_val, max_val = set_min_max(sample_set)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
