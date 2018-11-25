# Find the missing element

# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# the output should be 5 is the missing number

# the naive solution is brute force, and the complexity of this approach is O(N^2)


def finder(arr1,arr2):

    arr1.sort()
    arr2.sort()

    # zip() is a python builtin function
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]))



import collections

def finder2(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num]-=1

a1=[5,6,7,7]
a2=[5,7,7]
print(finder2(a1, a2))
