# Largest Continuous Sum
# Problem Given array of integers (positive and negative) find the largest continuous sum

# largest_cont_sum([1,2,-1,3,4,10,10,-10,-1])
# ==> 29

def largest_cont_sum(arr):

    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:

        current_sum = max(current_sum+num, num)

        max_sum = max(current_sum, max_sum)

    return max_sum


print(largest_cont_sum([1,2,-1,3,4,10,10,-10,-1]))

