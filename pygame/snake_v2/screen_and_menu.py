import pygame
from snake import Snake
from option import options
from game_run import Game_runner
class Menu:
    def __init__(self):
        self.GameMode = 0
        self.width = 680
        self.height = 600
        self.title_font = pygame.font.SysFont("Arial", 40)
        self.font = pygame.font.SysFont("Arial", 20)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.size = 40
        self.option = options()
        self.snake = Snake(self.option.snake_main)
        self.runner = Game_runner(self.screen, self.snake)
        
    def Screen(self):
        for x in range(0, self.width, self.size):
            for y in range(0, self.height, self.size):
                color = (50, 50, 50) if (x // self.size + y // self.size) % 2 == 0 else (60, 60, 60)
                rect = pygame.Rect(x, y, self.size, self.size)
                screen = pygame.draw.rect(self.screen, color, rect)
        if self.GameMode == 0:
            self.text()
        elif self.GameMode == 1:
            self.runner.draw_start()
        elif self.GameMode == 2:
            self.Option()
        
    def Option(self):
        for x in range(0, self.width):
            for y in range(0, self.height - 100, self.size):
                color = ("grey") if ((100 < x < 140) or (y // 40) % 2 == 1) else ("white")
                rect = pygame.Rect(x, y, self.size, self.height)
                pygame.draw.rect(self.screen, color, rect)
        equip = self.font.render("equiped \/", True, "black")
        choice = self.font.render("choices | chose by clikcing | \/", True, "black")
        back = self.font.render("[esc] press 'esc' to return to the menu", True, "black")
        self.screen.blit(back, (self.width // 2 - back.get_width() + 140, 500))
        self.screen.blit(choice, (550//2 + 140 - choice.get_width(), 0))
        self.screen.blit(equip, (100//2 - equip.get_width()//2, 0))
        self.screen.blit(self.snake.head, (0, 80))
        x_ofset = 140
        self.snake_rects = []
        for snake in self.option.snake:
            rect = pygame.Rect(x_ofset, 80, snake.get_width(), snake.get_height())
            self.screen.blit(snake, (x_ofset, 80))
            self.snake_rects.append(rect)
            x_ofset += snake.get_width() + 10
        
    def text(self):
        title = self.title_font.render("This is Snake v2.0", True, "Black")
        play = self.font.render("[1] Play", True, "Black")
        option = self.font.render("[2] Options", True, "Black")
        self.screen.blit(title, (self.width//2 - title.get_width()//2, 0))
        self.rect_play = play.get_rect(topleft=(self.width//2 - play.get_width()//2, 100))
        self.screen.blit(play, self.rect_play)
        self.rect_option = option.get_rect(topleft=(self.width//2 - option.get_width()//2, 200))
        self.screen.blit(option, self.rect_option)
        self.rects = [(self.rect_play), (self.rect_option)]
        
    def draw_snake(self):
        self.screen.blit(self.snake.head, self.snake.start)
        