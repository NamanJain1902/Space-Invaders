import pygame
import os

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'images') # The resource folder path
image_path = os.path.join(resource_path, 'icon') # The image folder path
bg_path = os.path.join(resource_path, 'background') # The image folder path
# def bg_info():
# Creating Screen
screen = pygame.display.set_mode((800, 600))

# Title and Image
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(os.path.join(image_path, 'ufo.png'))
pygame.display.set_icon(icon)

# Background
background = pygame.image.load(os.path.join(bg_path, 'bg.jpg')) 