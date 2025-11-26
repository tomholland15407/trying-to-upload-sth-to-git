def compress(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        while i < (len(s)-1) and s[i] == s[i+1]:
            count += 1
            i += 1
        result += s[i] + str(count)
        i += 1
    return result
s = input()
d = compress(s)
print(d)