import pygame

class Menu:
    def __init__(self):
        self.GameMode = None
        self.width = 800
        self.height = 900
        self.title_font = pygame.font.SysFont("Arial", 40)
        self.font = pygame.font.SysFont("Arial", 20)
        self.screen = pygame.display.set_mode((self.width, self.height))
        
    def Screen(self):
        if self.GameMode == None:
            pygame.draw.rect(self.screen, "Grey", (0, 0, self.width, self.height))
            self.text()
        
    def text(self):
        title = self.title_font.render("This is Snake v2.0", True, "Black")
        play = self.font.render("[1] Play")
        self.screen.blit(title, (self.width//2 - title.get_width()//2, 0))
        pass