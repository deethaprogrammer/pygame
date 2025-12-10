import pygame
pygame.init()

class Game_runner:
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        pass
    def move(self):
        self.snake.move()
        self.screen.blit(self.snake.head, self.snake.start)
    def draw_start(self):
        self.screen.blit(self.snake.head, self.snake.start)