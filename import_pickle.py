import pickle
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
with open('lists_ex6.pkl', 'wb') as file:
    pickle.dump((a,b), file)
with open('lists_ex6.pkl', 'rb') as file:
    c, d = pickle.load(file)
total = [i+j for i,j in zip(c,d)]
print(total)
