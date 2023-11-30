#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Initialize the sum to zero
    total_sum = 0

    # Iterate through command-line arguments and add them to the sum
    for arg in sys.argv[1:]:
        total_sum += int(arg)

    # Print the result
    print(total_sum)
