sentence = list(map(str, input().split()))
dict = {}
for word in sentence:
    dict[word] = dict.get(word, -1) + 1
    print(dict[word], end=' ')

