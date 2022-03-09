#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: March 2022
# This program calculates the circumference of a circle
#   with radius inputted by the user

import Constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter radius of the circle (cm): "))

    # process
    circumference = Constants.Tau * radius

    # output
    print("")
    print("Its circumference is {0} cm².".format(circumference))

    print("\nDone.")


if __name__ == "__main__":
    main()
