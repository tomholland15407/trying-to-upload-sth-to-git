sentence = input('enter a sentence: ').lower().split()
dict = {}
for word in sentence:
    dict[word] = dict.get(word, 0) + 1
for key, value in dict.items():
    print(key + ': ' + str(value))
