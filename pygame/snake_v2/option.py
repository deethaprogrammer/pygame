import os
import pygame
pygame.init()
path = os.path.dirname(__file__)
asset = os.path.join(path, "assets")
snake = os.path.join(asset, "snake")
class options:
    def __init__(self):
        snakes = os.listdir(snake)
        
        snake_images = [os.path.join(snake, f) for f in snakes if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        
        self.snake = [pygame.transform.scale(pygame.image.load(img), (40, 40)) for img in snake_images]

        self.snake_main = self.snake[0] if self.snake else None