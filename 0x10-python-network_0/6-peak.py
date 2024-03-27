def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integers.
    A peak is defined as an element that is greater than or equal to its neighbors.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: A peak element if found, otherwise None.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]

