import pygame
# class defs():
def player(x, y):
    screen.blit(playerImg, (x, y))

def monster(x,y):
    screen.blit(monsterImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg,   (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,  (x + 16, y + 10))
