import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hwasubun')

image1 = pygame.image.load("image1.png")
image2 = pygame.image.load("image2.png")
image3 = pygame.image.load("image3.png")
image4 = pygame.image.load("image4.png")
image5 = pygame.image.load("image5.png")
image6 = pygame.image.load("image6.png")

deck = []
copy_deck = []

card_kind = [image1,image2,image3,image4,image5, image6]

for i in range(0, 10):
    random.shuffle(card_kind)
    deck.append(card_kind[0])

def matchDeck():
    
    for i in range(5):
        while(deck[i] == deck[i + 5]):

            for j in range(4 - i):
                deck[i + j] = deck[i + j + 1]
                deck[i + j + 5] = deck[i + j + 5 + 1]

            random.shuffle(card_kind)
            deck[4] = card_kind[0]
            deck[9] = card_kind[1]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_RIGHT:
                copy_deck = deck[:] # value copy
                for i in range(4): # 0 1 2 3
                    copy_deck[5 + i + 1] = deck[5 + i]
                    if (i == 3):
                        copy_deck[5] = deck[5 + i + 1]
                deck = copy_deck[:]

                matchDeck()

            if event.key == pygame.K_LEFT:
                copy_deck = deck[:] # value copy
                for i in range(1, 5): # 1 2 3 4
                    copy_deck[5 + i - 1] = deck[5 + i]
                    if (i == 4):
                        copy_deck[5 + i] = deck[5]
                deck = copy_deck[:]

                matchDeck()

        if event.type == pygame.MOUSEBUTTONUP:
            x,y = event.pos
            grid_x = x / 85

            value = grid_x % 5
            temp = deck[value]
            deck[value] = deck[value + 5]
            deck[value + 5] = temp

            matchDeck()

    for x in range(5):
        for y in range(2):
            img = deck[y * 5 + x]
            screen.blit(img, (x * 85, y * 140))

    pygame.display.update()

