print(f'Hello to my Python world\n')
feel = input('How am i feeling today? \n')

secret = 'happy' or 'Happy'

while feel.lower() != secret:
    feel = input(f'Hung is not feeling {feel}, please try again. \n ')

print(f'You got it right! Hung is definitely feeling {feel}! THANKS!\n')


