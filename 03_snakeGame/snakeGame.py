import sys, pygame
import random
import time

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
    'x' : 1,
    'y' : 0,
    'dir' : 'RIGHT',
    'img' : snakeHeadImage
}

snake.append(head)

apple = {
        'x' : 3,
        'y' : 0,
        'img' : appleImage,
        'used' : 0
        }

map.append(apple)

def DrawLines():
    for i in range(11):
        v = 50 * i + 1
        pygame.draw.line(screen, black, [0, v], [500, v], 3)
        pygame.draw.line(screen, black, [v, 0], [v, 500], 3)

def GenerateApple():

    shuffle = [1,2,3,4,5,6,7,0]
    shuffle * 2
    random.shuffle(shuffle)

    if(shuffle[0] == 0 and map[0]['used'] == 1):
        map[0]['x'] = shuffle[1]
        map[0]['y'] = shuffle[2]
        map[0]['used'] = 0

def MeetApple():
    if(snake[0]['x'] == map[0]['x'] and snake[0]['y'] == map[0]['y'] and map[0]['used'] == 0):
        map[0]['used'] = 1
        GrowUp()

def GrowUp():
    tailValue = len(snake) - 1

    if( snake[0]['dir'] == 'RIGHT'):
        xValue = snake[tailValue]['x']
        yValue = snake[tailValue]['y']

    if( snake[0]['dir'] == 'LEFT'):
        xValue = snake[tailValue]['x']
        yValue = snake[tailValue]['y']

    if( snake[0]['dir'] == 'UP'):
        xValue = snake[tailValue]['x']
        yValue = snake[tailValue]['y']

    if( snake[0]['dir'] == 'DOWN'):
        xValue = snake[tailValue]['x']
        yValue = snake[tailValue]['y']

    body = {
    'x' : xValue,
    'y' : yValue,
    'img' : snakeBodyImage
    }

    snake.append(body)

def Move():
    if(snake[0]['x'] < 9 and snake[0]['x'] >= 0 and snake[0]['y'] >= 0 and snake[0]['y'] < 9):
        for v in range(len(snake) - 1, 0, -1):
            snake[v]['x'] = snake[v - 1]['x']
            snake[v]['y'] = snake[v - 1]['y']

        if( snake[0]['dir'] == 'RIGHT'):
            snake[0]['x'] += 1

        if( snake[0]['dir'] == 'LEFT'):
            snake[0]['x'] -= 1

        if( snake[0]['dir'] == 'UP'):
            snake[0]['y'] -= 1

        if( snake[0]['dir'] == 'DOWN'):
            snake[0]['y'] += 1

    time.sleep(0.2)
    # apple generate
    GenerateApple()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_RIGHT:
                if(snake[0]['dir'] != 'LEFT'):
                    snake[0]['dir'] = 'RIGHT'
                
            if event.key == pygame.K_LEFT:
                if(snake[0]['dir'] != 'RIGHT'):
                    snake[0]['dir'] = 'LEFT'

            if event.key == pygame.K_UP:
                if(snake[0]['dir'] != 'DOWN'):
                    snake[0]['dir'] = 'UP'

            if event.key == pygame.K_DOWN:
                if(snake[0]['dir'] != 'UP'):
                    snake[0]['dir'] = 'DOWN'

    screen.fill(white)

    DrawLines()
    MeetApple()
    Move()

    for x in range(len(snake)):
        img = snake[x]['img']
        screen.blit(img, (snake[x]['x'] * 50 + 6, snake[x]['y'] * 50 + 6))

    for y in range(len(map)):
        if(map[y]['used'] == 0):
            img = map[y]['img']
            screen.blit(img, (map[y]['x'] * 50 + 6, map[y]['y'] * 50 + 6))

    pygame.display.flip()
