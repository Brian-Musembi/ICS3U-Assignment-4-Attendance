#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: May 2021
# This program asks the user to enter the number of classes held and attended
#     and tells them if they can do the exam or not


def main():
    # This function calculates if student can write exam

    # input
    number = input("Enter the total number of classes held: ")
    number2 = input("Enter the total number of classes you have attended: ")
    print("")

    # process
    try:
        classes_held = int(number)
        classes_attended = int(number2)

        percentage = ((classes_attended / classes_held) * 100)
        print("You have attended {0}% of all classes".format(percentage))
        print("")

        if (percentage >= 75.0):
            print("Amazing! You are eligible to take the exam.")
            print("")

        else:
            print("Sorry but you aren't eligible enough to take the exam.")
            print("")

    except ValueError:
        print("Invalid input.")

    finally:
        print("Thank you for your input.")


if __name__ == "__main__":
    main()
