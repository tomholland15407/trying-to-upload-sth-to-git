import random

print('Tối nay ta đi đâu nhờ?')
print('Hãy nhập những nơi bạn muốn đi vào tối nay với mình nhé - dooki, gogi, haidilao, ... Khi nào nhập xong, điền "xong" nhé!\n')

names = []

while True:
    name = input('Một nơi bạn muốn đến là: ')
    if name.lower().strip() == 'xong':
        break
    elif len(name.strip()) == 0:
        print('Hình như đây không phải là một điểm đến.')
    else:
        names.append(name)

if len(names) == 0:
    print('Hic bạn chưa điền nơi nào cả:(')
else:
    winner = random.choice(names)
    print(f'\nHưng sẽ đi {winner} vào tối nay với bạn nhé. MISS u.')
