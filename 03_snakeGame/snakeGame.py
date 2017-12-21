import sys, pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('snake')

map = []
snake = []

direction = ['UP','DOWN','LEFT','RIGHT']

# colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Images
snakeHeadImage = pygame.image.load("snakeHead.png")
snakeBodyImage = pygame.image.load("snakeBody.png")
appleImage = pygame.image.load("apple.png");

head = {
    'x' : 0,
    'y' : 0,
    'dir' : 'RIGHT',
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

def DrawLines(x, y):
    for i in range(11):
        v = 50 * i + 1
        pygame.draw.line(screen, black, [0, v], [500, v], 3)
        pygame.draw.line(screen, black, [v, 0], [v, 500], 3)

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

    DrawLines(2, 2)

    for x in range(2):
        img = snake[x]['img']
        screen.blit(img, (snake[x]['x'] * 50 + 6, snake[x]['y'] * 50 + 6))

    pygame.display.flip()
