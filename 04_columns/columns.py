# 가로, 세로, 대각선으로 3개의 블록이 같으면 깨진다.
# 빨, 주, 노, 초, 파, 보
# 변경을 누르면 아래꺼 빼서 맨 위로 보냄
#  3   ->    1
#  2   ->    3
#  1   ->    2
# 가로 6칸 
# 세로 13칸
# 블록 하나 3칸

import sys, pygame
import random
import time

# colors
white = (255, 255, 255)

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
block_list = []
next_block = []
move_list = []

#image
redTileImage = pygame.image.load("redTile.png")
orangeTileImage = pygame.image.load("orangeTile.png")
yellowTileImage = pygame.image.load("yellowTile.png")
greenTileImage = pygame.image.load("greenTile.png")
blueTileImage = pygame.image.load("blueTile.png")
purpleTileImage = pygame.image.load("purpleTile.png")


block = {
    'x' : 0,
    'y' : 0,
    'color' : 'red',
    'img' : redTileImage,
    'isMove' : True
}

block_list.append(block)

block2 = {
    'x' : 0,
    'y' : 1,
    'color' : 'blue',
    'img' : blueTileImage,
    'isMove' : True
}

block_list.append(block2)

block3 = {
    'x' : 0,
    'y' : 2,
    'color' : 'green',
    'img' : greenTileImage,
    'isMove' : True
}

block_list.append(block3)

def MoveRight():
    for x in range(len(block_list)):
        if(block_list[x]['isMove'] == True):
            block_list[x]['x'] += 1

def MoveLeft():
    for x in range(len(block_list)):
        if(block_list[x]['isMove'] == True):
            block_list[x]['x'] -= 1

def MoveDown():
    for x in range(len(block_list)):
        if(block_list[x]['isMove'] == True):
            block_list[x]['y'] += 1

    time.sleep(0.4)

def Move():
    for x in range(len(move_list)):
        if(move_list[x] == 'Left'):
            MoveLeft()
        if(move_list[x] == 'Right'):
            MoveRight()
        if(move_list[x] == 'Down'):
            MoveDown()

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('columns')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                MoveRight()
            if event.key == pygame.K_LEFT:
                MoveLeft()
        
    screen.fill(white)

    for x in range(len(block_list)):
        img = block_list[x]['img']
        screen.blit(img, (block_list[x]['x'] * 50 + 30, block_list[x]['y'] * 50))

    moveDown()

    pygame.display.flip()