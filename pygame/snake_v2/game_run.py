#game_run.py
import pygame
from food import Food
pygame.init()

class Game_runner:
    def __init__(self, screen, snake, food_img):
        self.screen = screen
        self.snake = snake
        self.food = food_img
        
    def move(self):
        result = self.snake.move()
        if (self.snake.x, self.snake.y) == self.food.get_pos():
            self.snake.grow()
            self.food.respawn(
                snake_body=self.snake.body,
                snake_head=(self.snake.x, self.snake.y)
            )

        
        # Draw head
        self.screen.blit(self.snake.head, self.snake.start)

        if self.snake.aligned_this_frame:
            for segment in self.snake.body:
                pygame.draw.rect(
                    self.screen,
                    (0, 200, 0),
                    pygame.Rect(segment[0], segment[1], self.snake.width, self.snake.height)
                )
        #draw food
        self.food.draw(self.screen)

        if result == "dead":
            print("GAME OVER")

        
    def draw_start(self):
        self.screen.blit(self.snake.head, self.snake.start)
        self.food.draw(self.screen)