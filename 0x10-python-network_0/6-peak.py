#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of integers.

    Returns:
    - The peak element if found, None otherwise.
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize variables
    left = 0
    right = len(list_of_integers) - 1

    # Binary search to find a peak
    while left < right:
        mid = (left + right) // 2

        # Check if the peak is on the right
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        # Check if the peak is on the left
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        # If neither, we've found a peak
        else:
            return list_of_integers[mid]

    # Return the peak (if only one element in the list)
    return list_of_integers[left]

# Example usage:
# list_of_integers = [1, 3, 20, 4, 1, 0]
# print(find_peak(list_of_integers))

