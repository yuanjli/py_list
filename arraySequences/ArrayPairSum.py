# Array Pair Sum

# input: pair_sum([1,3,2,2],4)
# output: (1,3) (2,2)

# we going to use the "set" data structure

def pair_sum(arr, k):

    # edge check
    if len(arr)<2:
        return

    # initializing the set
    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num, target), max(num, target))))

    # return len(output)
    return '\n'.join(map(str, list(output)))

print(pair_sum([1,3,2,2],4))