# Given a string, write a function that uses recursion to output a list of all the possible permutations of that string. 

# For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def permute(str):
    output = []

    if len(str) == 1:
        output = [str]
    else: 
        for i, let in enumerate(str):
            for perm in permute(s[:1] + s[i+1:]):

                output += [let + perm]

    return output