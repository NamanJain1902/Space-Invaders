import pygame
import random
# Player
playerImg = pygame.image.load("images/spirits/player.png")
player_X = 303
player_Y = 503
playerchange_X = 0

# Monster
monsterImg = pygame.image.load("images/spirits/monster.png")
monster_X = 303
monster_Y = 503
monsterchange_X = 0

# Enemy
enemyImg = pygame.image.load("images/spirits/enemy.png")
enemy_X = random.randint(0,764)
enemy_Y = random.randint(50,400)
enemychange_X = 8
enemychange_Y = 40

# Bullet
bulletImg = pygame.image.load("images/spirits/bullet.png")
bullet_X = random.randint(0,764)
bullet_Y = random.randint(50,400)
bulletchange_X = 8
bulletchange_Y = 40
bullet_state = "ready"