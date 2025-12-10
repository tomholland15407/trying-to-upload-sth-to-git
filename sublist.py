#  Core Concepts
# - Backtracking
# - Backtracking is a recursive technique where you explore all possible choices step by step.
# - At each step, you decide whether to include or exclude the current element, then recurse further.
# - Recursive Function (backtrack)
# - The function takes two parameters:
# - index: the current position in the array.
# - path: the current subset being built.
# - It explores two branches:
# - Include arr[index] in the subset.
# - Exclude arr[index] from the subset.
# - Base Case
# - When index == len(arr), you’ve considered all elements.
# - At this point, path represents one complete subset, so it’s added to sets.
# - Path Building
# - path + [arr[index]] creates a new list with the current element included.
# - path alone represents the branch where the element is excluded.
# - Result
# - After recursion finishes, sets contains all possible subsets of the input array.

def generate_sets(arr):
    sets = []
    def backtrack(index, path):
        if index == len(arr):
            sets.append(path)
        else:
            backtrack(index + 1, path + [arr[index]])
            backtrack(index + 1, path)
    backtrack(0, [])
    return sets

if __name__ == '__main__':
    t = list(map(str, input().split()))
    k = int(input())

    subsets = generate_sets(t)

    for s in subsets:
        if len(s) == k:
            print(s)