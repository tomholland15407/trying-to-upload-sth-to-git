sentence = input('enter a sentence: ').lower().split()
s = ' '.join(sentence)
#Hello world ! Welcome to the world . The world greets you


word = input('enter a word: ').lower()
a = sentence.count(word)

b = s.find(word)

if a > 0:
    print(f"'{word}' firstly occurs at position {b}, number of occurrences {a}")
else:
    print(f"'{word} does not occur in the sentence.'")



