#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, calculating the average of 10 random numbers

import random


def main():
    # This function calculates the average
    random_number = []

    # input
    for loop_counter in range(0, 10):
        single_number = random.randint(1, 100)
        random_number.append(single_number)

    # process & output
    average_sum = 0
    for loop_counter in range(len(random_number)):
        print("The random number is: {}".format(random_number[loop_counter]))
        average_sum = average_sum + random_number[loop_counter]
    average = average_sum / len(random_number)
    print("\nThe average is {}".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
