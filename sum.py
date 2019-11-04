#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: November 2019
# This is the calculate sum program


def main():
    # This function runs the calculate sum program

    # Variables
    adding_num = 0

    # Input
    num = int(input("How many numbers are you going to add: "))
    print("")

    # Process
    for counter in range(num):
        number = int(input("Enter a number to add: "))
        if number < 0:
            continue

        adding_num = adding_num + number

    # Output
    print("")
    print("Sum of just the positive numbers is = ", adding_num)


if __name__ == "__main__":
    main()
