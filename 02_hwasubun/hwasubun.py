import sys, pygame
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

card_kind = [image1,image2,image3,image4,image5, image6];

for i in range(0, 10):
    random.shuffle(card_kind)
    deck.append(card_kind[0])

is_first_select = False
is_second_select = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                deck[5 + x]
            if event.key == pygame.K_RIGHT:
                deck[5 + x]
    for x in range(5):
        for y in range(2):
            img = deck[y * 5 + x]
            screen.blit(img, (x * 85 + 30, y * 140 + 30))

    pygame.display.update()