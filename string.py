import sys
import math


###  Bracket match:
def bracket_match(bracket_string):
    if len(bracket_string) == 0:
        return 0
    left = 0
    right = 0
    for i in range(len(bracket_string)):
        if bracket_string[i] == '(':
            right += 1
        elif bracket_string[i] == ')':
            left += 1
    return abs(right - left)


print('=> bracket marching: ')
print(bracket_match('((()))()())))))'))


###
def insertion_sort(aList):
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    aList[k] = tmp


my_list = [5, 2, 6, 7, 12, 18, 21, 3, 6, 9]
insertion_sort(my_list)


def binary_search(data, target):
    # Track minimum and maximum indexes
    min_index = 0
    max_index = len(data) - 1

    # Loop until we...
    # Find the target! Yay!
    # Have the condition min_index > max_index
    while min_index <= max_index:

        # Formulate my guess
        # Note: Double // means integer division
        guess = (min_index + max_index) // 2

        # Check if we found the target value
        if data[guess] == target:

            # We found it - use return, which breaks out of the function
            return guess

        elif data[guess] < target:

            # The target value is higher than my guess
            # So, guess + 1 is my new min_index
            min_index = guess + 1

        else:

            # The target is lower than the guess
            # So, we set the new max_index to guess - 1
            max_index = guess - 1

    # Negative one is generally understood to be a "bad" index, AKA not found!
    return -1


# Try out the function
test_target = 14
test_data = [1, 2, 4, 5, 7, 9, 10, 11, 13, 15, 16, 18, 100, 120]
print("Found target value", test_target, "at index", binary_search(test_data, test_target))






