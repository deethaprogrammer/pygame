#food.py
import pygame
import random

class Food:
    def __init__(self, food_img, width=680, height=600, cell_size=40):
        self.img = food_img
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.x = 0
        self.y = 0
        self.respawn()
    
    def respawn(self, snake_body=None, snake_head=None):
        x_grid = self.width // self.cell_size
        y_grid = self.height // self.cell_size
        while True:
            x = random.randint(0, x_grid - 1) * self.cell_size
            y = random.randint(0, y_grid - 1) * self.cell_size

            # If no snake info provided, just accept
            if snake_body is None:
                break

            # Check collision with head or body
            if (x, y) != snake_head and (x, y) not in snake_body:
                break

        self.x = x
        self.y = y

    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def get_pos(self):
        return (self.x, self.y)