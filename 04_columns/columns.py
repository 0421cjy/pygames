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

TARGET_FPS = 3

# colors
white = (255, 255, 255)

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
block_list = []
cur_move_block_list = []
next_block = []
move_direction = []

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

cur_move_block_list.append(block)

block2 = {
    'x' : 0,
    'y' : 1,
    'color' : 'blue',
    'img' : blueTileImage,
    'isMove' : True
}

cur_move_block_list.append(block2)

block3 = {
    'x' : 0,
    'y' : 2,
    'color' : 'green',
    'img' : greenTileImage,
    'isMove' : True
}

cur_move_block_list.append(block3)

dir = {
    'dir' : 'Down'
    }

move_direction.append(dir)

def MoveRight():
    if(move_direction[0]['dir'] == 'Stop'):
        return

    for x in range(len(cur_move_block_list)):
        if(cur_move_block_list[x]['isMove'] == True):
            cur_move_block_list[x]['x'] += 1

def MoveLeft():
    if(move_direction[0]['dir'] == 'Stop'):
        return

    for x in range(len(cur_move_block_list)):
        if(cur_move_block_list[x]['isMove'] == True):
            cur_move_block_list[x]['x'] -= 1

def MoveDown():
    if(move_direction[0]['dir'] == 'Stop'):
        return

    for x in range(len(cur_move_block_list)):
        if(cur_move_block_list[x]['isMove'] == True):
            cur_move_block_list[x]['y'] += 0.5
        
        if(cur_move_block_list[x]['y'] == 5):
            #일정 위치가 되거나 기존 블록과 충돌하면 정지한다.
            move_direction[0]['dir'] = 'Stop'
            MoveToFix()

def Move():
    if(move_direction[0]['dir'] == 'Left'):
        MoveLeft()
        move_direction[0]['dir'] = 'Down'
    if(move_direction[0]['dir'] == 'Right'):
        MoveRight()
        move_direction[0]['dir'] = 'Down'
    if(move_direction[0]['dir'] == 'Down'):
        MoveDown()

def PrintPos():
    textSurfaceObj = fontObj.render('posX : {0}, posY : {1}'.format(cur_move_block_list[2]['x'], cur_move_block_list[2]['y']) , True, (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (350, 15)
    screen.blit(textSurfaceObj, textRectObj)

def MoveToFix():
    for x in range(len(cur_move_block_list)):
        block_list.append(cur_move_block_list[x])

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((400,700))
pygame.display.set_caption('columns')

#font
fontObj = pygame.font.Font('font/nanum.ttf', 11)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                move_direction[0]['dir'] = 'Right'
            if event.key == pygame.K_LEFT:
                move_direction[0]['dir'] = 'Left'
        
    screen.fill(white)

    for x in range(len(cur_move_block_list)):
        img = cur_move_block_list[x]['img']
        screen.blit(img, (cur_move_block_list[x]['x'] * 50, cur_move_block_list[x]['y'] * 50))

    for x in range(len(block_list)):
        img = block_list[x]['img']
        screen.blit(img, (block_list[x]['x'] * 50, block_list[x]['y'] * 50))

    Move()
    PrintPos()
    clock.tick(TARGET_FPS)

    pygame.display.flip()