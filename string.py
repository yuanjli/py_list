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




