import sys, pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((400, 300))
 
back = pygame.image.load("back.png")
red = pygame.image.load("red.png")
orange = pygame.image.load("orange.png")
blue = pygame.image.load("blue.png")
green = pygame.image.load("green.png")

card_color = [red, orange, blue, green] * 2
random.shuffle(card_color)

deck = []

for color in card_color:
    card = {
        'front': color,
        'isFront': False
        }
    deck.append(card)

is_first_select = False
is_second_select = False

while 1:
    is_selected = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            grid_x = x / 55 
            grid_y = y / 55
            select_card = deck[grid_y * 4 + grid_x]
            if select_card['isFront'] != True:
                is_selected = True

    if is_selected:
        grid_x = x / 55 
        grid_y = y / 55

        select_card = deck[grid_y * 4 + grid_x]
        select_card['isFront'] = True

    for x in range(4):
        for y in range(2):
            card = deck[y * 4 + x]

            img = back
            if card['isFront']:
                img = card['front']

            screen.blit(img, (x * 55, y * 55))

    pygame.display.flip()
 
    if is_selected:
        if is_first_select == False:
            first_select = select_card
            is_first_select = True
        else:
            second_select = select_card
            is_second_select = True

        if (is_first_select == True & is_second_select == True):
            if(first_select['front'] != second_select['front']):
                time.sleep(1)
                first_select['isFront'] = False
                second_select['isFront'] = False
                is_selected = False
                is_first_select = False
                is_second_select = False
            else:
                time.sleep(1)
                is_selected = False
                is_first_select = False
                is_second_select = False