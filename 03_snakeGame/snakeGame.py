import sys, pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('snake')

map = []
snake = []

# 상하좌우
direction = ['UP','DOWN','LEFT','RIGHT']

# color
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# 이미지
snakeHeadImage = pygame.image.load("snakeHead.png")
snakeBodyImage = pygame.image.load("snakeBody.png")
appleImage = pygame.image.load("apple.png");

head = {
    'x' : 0,
    'y' : 0,
    #'dir' : 'RIGHT',
    'img' : snakeHeadImage
}

snake.append(head)

body = {
    'x' : 1,
    'y' : 0,
    'img' : snakeBodyImage
}

snake.append(body)

clock = pygame.time.Clock()
clock.tick(10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                snake[1]['x'] = snake[0]['x']
                snake[1]['y'] = snake[0]['y']
                snake[0]['x'] += 1;

            if event.key == pygame.K_LEFT:
                snake[1]['x'] = snake[0]['x']
                snake[1]['y'] = snake[0]['y']
                snake[0]['x'] -= 1;

            if event.key == pygame.K_UP:
                snake[1]['x'] = snake[0]['x']
                snake[1]['y'] = snake[0]['y']
                snake[0]['y'] -= 1;

            if event.key == pygame.K_DOWN:
                snake[1]['x'] = snake[0]['x']
                snake[1]['y'] = snake[0]['y']
                snake[0]['y'] += 1;

    screen.fill(white)

    pygame.draw.line(screen, black, [0,0], [100,0], 3)
    pygame.draw.line(screen, black, [0,0], [0,100], 3)
    pygame.draw.line(screen, black, [100,0], [100,100], 3)
    pygame.draw.line(screen, black, [0,100], [100,100], 3)

    pygame.draw.line(screen, black, [0,50], [100,50], 3)
    pygame.draw.line(screen, black, [50,0], [50,100], 3)

    for x in range(2):
        img = snake[x]['img']
        screen.blit(img, (snake[x]['x'] * 50 + 6, snake[x]['y'] * 50 + 6))

    pygame.display.flip()


def DrawLines(x, y):
    for i in range(x):

        for j in range(y):
