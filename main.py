import pygame
import random
import sys
# sys.path.insert(0, "./models/")
# sys.path.insert(0, "./modules/")
import os.path
print(os.path.dirname(__file__))    
# Initialize pygame
pygame.init()
from modules.defs import *
from models.bg_info import *
from models.sprite_info import *

running = True
while running:
    # RGB
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    # player_Y += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            # to check if it's right or left
            if event.key == pygame.K_RIGHT:
                playerchange_X = 10
                # print("r w")
            if event.key == pygame.K_LEFT:
                playerchange_X = -10
                # print("l w")
            if event.key == pygame.K_SPACE:
                fire_bullet(player_X, bullet_Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                # print('\nReleasing key')
                playerchange_X = 0
    
    # Player
    player_X += playerchange_X
    if player_X < 0:
        player_X = 0 
    if player_X > 736:
        player_X = 736
    
    # Enemy 
    enemy_X += enemychange_X
    if enemy_X < 0:
        enemychange_X = 8
        enemy_Y += enemychange_Y 
    if enemy_X > 736:
        enemychange_X = -8
        enemy_Y += enemychange_Y


    # Bullet Movement
    if bullet_Y <= 0:
        bullet_Y = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        fire_bullet(player_X, bullet_Y)
        bullet_Y -= bulletchange_Y

    player (player_X, player_Y)
    monster(player_X, player_Y)
    enemy  (enemy_X, enemy_Y)


    pygame.display.update()