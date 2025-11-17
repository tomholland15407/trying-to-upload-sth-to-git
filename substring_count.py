n = list(input())
''' Given a string str, we are interested in its substrings that have the same first and last character.
 Write a function substrings_count(str) to count the number of such substrings.
Example:
Input:  abcab
Output: 7
'''
a = 0
for i,t in enumerate(n):
    for j,s in enumerate(n):
        if t == s and j>=i:
            a += 1
print(a)