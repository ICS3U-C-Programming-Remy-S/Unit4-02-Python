#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Nov 8, 2023
# This program will ask the user
# for a integer and it will tell them the factorial
# of the number it with try catch


def main():
    # initialize counter and factorial variables
    factorial = 1
    counter = 1

    # Get the user number as a string and display message about program
    print(
        "This program will ask the user for a integer and it will tell them the factorial"
    )
    print("of the number.")
    user_num_str = input("Please enter a positive integer: ")

    # Catch if the user number is something wrong
    try:
        # Convert user number as a string to int
        user_num_int = int(user_num_str)

        if user_num_int < 0:
            # Message for negative user number
            print("\n{} is not a positive int.".format(user_num_int))

        # loop for factorial of user_number_as_int
        else:
            while True:
                # calculate factorial
                factorial = factorial * counter

                # display factorial to user and counter to user
                print("The loop ran {} times".format(counter))

                # increment counter
                counter = counter + 1
                if counter > user_num_int:
                    break

            # display factorial to user and counter to user
            print("\nThe factorial of {} is {}".format(user_num_int, factorial))

    # Display a message to the user if they entered something that is not valid
    except Exception:
        # Message for invalid user number
        print("\n{} is not a valid int.".format(user_num_str))


if __name__ == "__main__":
    main()
