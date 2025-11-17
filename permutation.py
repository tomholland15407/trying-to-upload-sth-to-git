'''''Exercise 8: Given an integer n, write a program to generate all permutations of 1, 2, ..., n
in lexicographic order (elements of a permutation are separated by a SPACE character).
Example
Input
3
Output
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
def generate_permutations(n):
    def backtrack(path, used):
        if len(path) == n:
            print(' '.join(map(str, path)))
            return
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                path.append(i)
                backtrack(path, used)
                path.pop()
                used[i] = False

    used = [False] * (n + 1)
    backtrack([], used)

# Example usage:
n = int(input("Enter a number: "))
generate_permutations(n)
