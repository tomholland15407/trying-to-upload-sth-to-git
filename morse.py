import pygame
import time

MORSE_DICT = {
    '·–': 'A', '–···': 'B', '–·–·': 'C', '–··': 'D', '·': 'E',
    '··–·': 'F', '––·': 'G', '····': 'H', '··': 'I', '·–––': 'J',
    '–·–': 'K', '·–··': 'L', '––': 'M', '–·': 'N', '–––': 'O',
    '·––·': 'P', '––·–': 'Q', '·–·': 'R', '···': 'S', '–': 'T',
    '··–': 'U', '···–': 'V', '·––': 'W', '–··–': 'X', '–·––': 'Y', '––··': 'Z',
    '–––––': '0', '·––––': '1', '··–––': '2', '···––': '3', '····–': '4',
    '·····': '5', '–····': '6', '––···': '7', '–––··': '8', '––––·': '9'
}

pygame.init()
screen = pygame.display.set_mode((1300,600))
pygame.display.set_caption('morse it2000')
font = pygame.font.SysFont(None, 48)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

morse_sequence = ""
translated_text = ""
current_letter = ""
threshold = 0.3
letter_pause = 1.5

running = True
space_pressed_time = None
last_input_time = time.time()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space_pressed_time = time.time()

        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            if space_pressed_time:
                duration = time.time() - space_pressed_time
                symbol = '·' if duration < threshold else '–'
                current_letter += symbol
                morse_sequence += symbol + '   '
                space_pressed_time = None
                last_input_time = time.time()


    if current_letter and (time.time() - last_input_time > letter_pause):
        translated_char = MORSE_DICT.get(current_letter, '?')
        translated_text += translated_char
        current_letter = ""
        morse_sequence += '       '

    morse_text = font.render(morse_sequence, True, BLACK)
    translated = font.render("Translation: " + translated_text, True, BLACK)
    screen.blit(morse_text, (20, 80))
    screen.blit(translated, (20, 150))
    pygame.display.flip()

pygame.quit()