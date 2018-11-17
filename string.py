
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