# - Problem: Compute the sum of all elements in a list.
# - Base case: If the list is empty, the sum is 0.
# - Recursive case:
# - Take the first element of the list.
# - Add it to the sum of the remaining elements (the rest of the list).

def sum_of_list(list):
    if list == []:
        return 0
    else:
        return list[0] + sum_of_list(list[1:])
print(sum_of_list([1, 2, 3, 4, 5, 6, 7]))