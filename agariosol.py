import pygame # подключаем библиотеку
import sys # подключаем модуль для 
import time
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(400, 400, 50, 50)
player_img_orig = pygame.image.load('steve.png')
player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
enemy = pygame.Rect(50, 50, 30, 30)
enemy_img = pygame.image.load('creeper.png')
enemy_img = pygame.transform.scale(enemy_img, (enemy.width, enemy.height))

directions = 'none'
directionc = 'none'

while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                directions = 'right'
            elif e.key == pygame.K_LEFT:
                directions = 'left'
            elif e.key == pygame.K_UP:
                directions = 'up'
            elif e.key == pygame.K_DOWN:
                directions = 'down'
            elif e.key == pygame.K_d:
                directionc = 'right'
            elif e.key == pygame.K_a:
                directionc = 'left'
            elif e.key == pygame.K_w:
                directionc = 'up'
            elif e.key == pygame.K_s:
                directionc = 'down'
        if e.type == pygame.KEYUP:
            directions = 'none'
            directionc = 'none'

    if directions == 'right':
        player.x += 5
    elif directions == 'left':
        player.x -= 5
    elif directions == 'up':
        player.y -= 5
    elif directions == 'down':
        player.y += 5

    if directionc == 'right':
        enemy.x += 5
    elif directionc == 'left':
        enemy.x -= 5
    elif directionc == 'up':
        enemy.y -= 5
    elif directionc == 'down':
        enemy.y += 5


    if player.colliderect(enemy):
        enemy.x = randint(0, 470)
        enemy.y = randint(0, 470)
        player.width += 5
        player.height += 5
        player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))\

    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)
    pygame.display.update()
    clock.tick(60)