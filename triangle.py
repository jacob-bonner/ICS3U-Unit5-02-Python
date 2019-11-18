#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program calculates the area of a triangle


def calculate(base, height):
    # This function calculates the area of a triangle

    # Process
    area = (base*height)/2
    print("")
    print("The area of the triangle is {0}cm^2".format(area))


def main():
    # This function takes two inputs then calls the calculate function

    # Process
    while True:
        # Input
        base_from_user = input("Enter the base in cm here (integer): ")
        height_from_user = input("Enter the height in cm here (integer): ")

        try:
            base_from_user = int(base_from_user)
            height_from_user = int(height_from_user)
            calculate(base_from_user, height_from_user)
            if base_from_user == int(base_from_user) and \
               height_from_user == int(height_from_user):
                break
            else:
                print("Error, unable to process inputs")
        except Exception:
            print("Error, one or both inputs not integers")
            print("")


if __name__ == "__main__":
    main()
