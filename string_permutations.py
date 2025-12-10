# - Problem: Generate all possible permutations of the characters in a string.
# - Base case:
# - If the string has length 1, the only permutation is the string itself.
# - Recursive case:
# - For each character in the string:
# - Fix that character as the first character.
# - Recursively generate all permutations of the remaining substring (the string without that character).
# - Combine the fixed character with each of those smaller permutations.
#
# 🧩 Example (string = "abc")
# - Fix "a" → permutations of "bc" → "bc", "cb" → add "a" in front → "abc", "acb".
# - Fix "b" → permutations of "ac" → "ac", "ca" → add "b" in front → "bac", "bca".
# - Fix "c" → permutations of "ab" → "ab", "ba" → add "c" in front → "cab", "cba".
# - Final result: ["abc", "acb", "bac", "bca", "cab", "cba"].

string = input('Enter a string: ')

def string_permutations(string):
    if len(string) == 1:
        return string
    result = []
    for i in range(len(string)):
        first = string[i]
        rest = string[:i] + string[i+1:]
        for j in string_permutations(rest):
            result.append(first + j)
    return result

print(string_permutations(string))