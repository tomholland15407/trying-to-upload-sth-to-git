# - Problem: Search for a target value in a sorted list.
# - Base case:
# - If the list is empty, the target is not found.
# - If the middle element equals the target, return its position.
# - Recursive case:
# - If the target is smaller than the middle element, search the left half of the list.
# - If the target is larger than the middle element, search the right half of the list.
def binary_search(n, list, left=0, right=None):
    if right is None:
        right = len(list) - 1
    if left > right:
        return -1
    mid = (left+right) // 2
    if n == list[mid]:
        return mid
    elif n < list[mid]:
        return binary_search(n, list, left, mid-1)
    elif n > list[mid]:
        return binary_search(n, list, mid+1, right)

print(binary_search(3, []))