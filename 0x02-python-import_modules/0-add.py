#!/usr/bin/python3

def main():
    # Import the add function from add_0
    from add_0 import add

    # Define variables
    a = 1
    b = 2

    # Perform addition
    result = add(a, b)

    # Display the result using formatted string
    print("{:d} + {:d} = {:d}".format(a, b, result))

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
