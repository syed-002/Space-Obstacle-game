import pygame
import os
import sys
from pygame.locals import *
from config import *
pygame.init()

window = pygame.display.set_mode((1840, 1010))

pygame.display.set_caption(("Pygame"))

bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (1840, 1010))

safe = pygame.image.load('safe.jpg')
safe = pygame.transform.scale(safe, (1840, 70))

score_bar = pygame.image.load('safe.jpg')
score_bar = pygame.transform.scale(score_bar, (1840, 60))

walkRight = pygame.image.load('top_right.png')
walkRight = pygame.transform.scale(walkRight, (60, 60))

walkLeft = pygame.image.load('top_left.png')
walkLeft = pygame.transform.scale(walkLeft, (60, 60))

walkUp = pygame.image.load('top_up.png')
walkUp = pygame.transform.scale(walkUp, (60, 60))

walkDown = pygame.image.load('top_down.png')
walkDown = pygame.transform.scale(walkDown, (60, 60))

fixed_obstacle = pygame.image.load('fixed_obstacle.jpg')
fixed_obstacle = pygame.transform.scale(fixed_obstacle, (70, 70))

img_moving_obstacle = pygame.image.load('moving_obstacle.png')
img_moving_obstacle = pygame.transform.scale(img_moving_obstacle, (60, 60))

fixed1 = pygame.image.load('top_up.png')
fixed1 = pygame.transform.scale(fixed1, (60, 70))

fixed2 = pygame.image.load('top_down.png')
fixed2 = pygame.transform.scale(fixed2, (60, 70))

'''music = pygame.mixer.music.load('musicc.mp3')
pygame.mixer.music.play(-1)'''


x = 50
y = 1010
width = 60
height = 60
vel_y = 80
vel_x = 15
up = False
down = False
left = False
right = False

collide1 = 0
collide2 = 0

moving_x1 = 900
moving_y1 = 70

moving_x2 = 0
moving_y2 = 220

moving_x3 = 0
moving_y3 = 400

moving_x4 = 900
moving_y4 = 560

moving_x5 = 0
moving_y5 = 720

moving_x6 = 900
moving_y6 = 865

moving_vel = 50


def collide_1():
    global score
    if x > 1200 - 70 and x < 1200 + 70:
        if y > 150 - 70 and y < 150 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 1200 - 70 and x < 1200 + 70:
        if y > 470 - 70 and y < 470 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 1200 - 70 and x < 1200 + 70:
        if y > 790 - 70 and y < 790 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 320 - 70 and x < 320 + 70:
        if y > 150 - 70 and y < 150 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 320 - 70 and x < 320 + 70:
        if y > 470 - 70 and y < 470 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 320 - 70 and x < 320 + 70:
        if y > 790 - 70 and y < 790 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 50 - 70 and x < 50 + 70:
        if y > 310 - 70 and y < 310 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 1700 - 70 and x < 1700 + 70:
        if y > 310 - 70 and y < 310 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 1700 - 70 and x < 1700 + 70:
        if y > 630 - 70 and y < 630 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 900 - 70 and x < 900 + 70:
        if y > 310 - 70 and y < 310 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    if x > 900 - 70 and x < 900 + 70:
        if y > 630 - 70 and y < 630 + 70:
            collide1 = 1
            score -= 5
            message_display("collision")

    # moving_obstacle collision

    if x > moving_x1 - 60 and x < moving_x1 + 60:
        if y > moving_y1 - 60 and y < moving_y1 + 60:
            collide1 = 1
            score -= 10
            message_display("collision")

    if x > moving_x2 - 60 and x < moving_x2 + 60:
        if y > moving_y2 - 60 and y < moving_y2 + 60:
            collide1 = 1
            score -= 10
            message_display("collision")

    if x > moving_x3 - 60 and x < moving_x3 + 60:
        if y > moving_y3 - 60 and y < moving_y3 + 60:
            collide1 = 1
            score -= 10
            message_display("collision")

    if x > moving_x4 - 60 and x < moving_x4 + 60:
        if y > moving_y4 - 60 and y < moving_y4 + 60:
            collide1 = 1
            score -= 10
            message_display("collision")

    if x > moving_x5 - 60 and x < moving_x5 + 60:
        if y > moving_y5 - 60 and y < moving_y5 + 60:
            collide1 = 1
            score -= 10
            message_display("collision")

    if x > moving_x6 - 60 and x < moving_x6 + 60:
        if y > moving_y6 - 60 and y < moving_y6 + 60:
            collide1 = 1
            score -= 10
            message_display("collision")


def moving_obstacle():
    global moving_x1
    global moving_y1
    global moving_x2
    global moving_x3
    global moving_y2
    global moving_y3
    global moving_y4
    global moving_x4
    global moving_x5
    global moving_x6
    global moving_y5
    global moving_y6

    if moving_x1 <= 1840:
        window.blit(img_moving_obstacle, (moving_x1, moving_y1))
        moving_x1 += moving_vel
    else:
        moving_x1 = 0
        window.blit(img_moving_obstacle, (moving_x1, moving_y1))
        #moving_x1 += moving_vel

    if moving_x2 <= 1840:
        window.blit(img_moving_obstacle, (moving_x2, moving_y2))
        moving_x2 += moving_vel
    else:
        moving_x2 = 0

    if moving_x3 <= 1840:
        window.blit(img_moving_obstacle, (moving_x3, moving_y3))
        moving_x3 += moving_vel
    else:
        moving_x3 = 0

    if moving_x4 <= 1840:
        window.blit(img_moving_obstacle, (moving_x4, moving_y4))
        moving_x4 += moving_vel
    else:
        moving_x4 = 0

    if moving_x5 <= 1840:
        window.blit(img_moving_obstacle, (moving_x5, moving_y5))
        moving_x5 += moving_vel
    else:
        moving_x5 = 0

    if moving_x6 <= 1840:
        window.blit(img_moving_obstacle, (moving_x6, moving_y6))
        moving_x6 += moving_vel
    else:
        moving_x6 = 0


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((1840 / 2), (1010 / 2))
    window.blit(TextSurf, TextRect)


def redrawGame():
    window.fill((0, 0, 0))
    window.blit(bg, (0, 0))
    window.blit(score_bar, (0, 0))

    start = font.render('START', 1, (0, 0, 0))
    end = font.render('END', 1, (0, 0, 0))

    global score
    text = font.render('SCORE: ' + str(score), 1, (0, 0, 0))
    window.blit(text, (10, 10))

    window.blit(safe, (0, 150))
    window.blit(fixed_obstacle, (1200, 150))
    window.blit(fixed_obstacle, (320, 150))
    window.blit(safe, (0, 310))
    window.blit(fixed_obstacle, (50, 310))
    window.blit(fixed_obstacle, (1700, 310))
    window.blit(fixed_obstacle, (900, 310))
    window.blit(safe, (0, 470))
    window.blit(fixed_obstacle, (1200, 470))
    window.blit(fixed_obstacle, (320, 470))
    window.blit(safe, (0, 630))
    window.blit(fixed_obstacle, (1700, 630))
    window.blit(fixed_obstacle, (920, 630))
    window.blit(safe, (0, 790))
    window.blit(fixed_obstacle, (1200, 790))
    window.blit(fixed_obstacle, (320, 790))
    window.blit(safe, (0, 950))

    collide_1()
    moving_obstacle()

    global a
    global y
    global left
    global right
    global up
    global down
    global collide1
    global x
    global y
    global width
    global height
    global vel_y
    global vel_x

    round = 1
    reached_end = 0
    if y <= 60:
        reached_end = 1
        a = score
        score = 0
    if reached_end == 1:
        window.blit(end, (900, 990))
        window.blit(start, (900, 10))
    if y > 950:
        #reached_end = 0
        if reached_end == 0:
            if score > a:
                message_display("PLAYER_1 IS WINNER!")
            elif score < a:
                message_display("PLAYER_2 IS WINNER!")
            elif score == a:
                message_display("START THE GAME!")
        score = 0
    round += 1
    if round == 2:
        moving_vel = 100
    if round == 3:
        moving_vel = 125
    if round == 4:
        moving_vel = 150
    if round == 5:
        moving_vel = 200

    if reached_end == 0:
        window.blit(end, (900, 10))
        window.blit(start, (900, 990))

    if left:
        window.blit(walkLeft, (x, y))
    elif right:
        window.blit(walkRight, (x, y))
    elif up:
        window.blit(walkUp, (x, y))
    elif down:
        window.blit(walkDown, (x, y))

    window.blit(fixed1, (0, 950))
    window.blit(fixed2, (1780, 0))

    if collide1 == 1:
        x = 50
        y = 1010
        width = 60
        height = 60
        vel_y = 80
        vel_x = 15
        up = False
        down = False
        left = False
        right = False

        if left:
            window.blit(walkLeft, (x, y))
        elif right:
            window.blit(walkRight, (x, y))
        elif up:
            window.blit(walkUp, (x, y))
        elif down:
            window.blit(walkDown, (x, y))

        window.blit(fixed1, (0, 950))
        window.blit(fixed2, (1780, 0))

        collide1 = 0
    pygame.display.update()


# main loop
font = pygame.font.SysFont('comicsans', 30, True)
run = True
score = 0
count = 0
a = 0


while run:
    pygame.time.delay(50)
    global reached_end
    reached_end = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel_x:
        x -= vel_x
        left = True
        right = False
        up = False
        down = False

    elif keys[pygame.K_RIGHT] and x < 1840 - width:
        x += vel_x
        left = False
        right = True
        up = False
        down = False

    elif keys[pygame.K_UP] and y >= 10:
        if reached_end == 0:
            if count % 2 != 0:
                score += 5
            else:
                score += 10
                count += 1
        if reached_end == 1:
            if count % 2 != 0:
                score -= 5
            else:
                score -= 10
            count -= 1

        y -= vel_y
        up = True
        down = False
        left = False
        right = False
        if vel_y > (y):
            y += y

    elif keys[pygame.K_DOWN] and y < 1010 - height:
        if reached_end == 0:
            if count % 2 != 0:
                score += 5
            else:
                score += 10
                count += 1
        if reached_end == 1:
            if count % 2 != 0:
                score -= 5
            else:
                score -= 10
            count -= 1
        y += vel_y
        up = False
        down = True
        left = False
        right = False
        if vel_y > (1840 - y):
            y += 1840 - y

    redrawGame()


pygame.quit()
