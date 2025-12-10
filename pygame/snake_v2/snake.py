import pygame

class Snake:
    def __init__(self, snake_head):
        self.original = snake_head
        self.head = snake_head
        self.width = 40
        self.height = 40
        self.speed = 10
        self.x = 160
        self.y = 320
        self.start = (self.x, self.y)
        self.dx = 0
        self.dy = 0
        self.next_dir = (0, 0)
        self.cell_size = 40
        self.body =[(0, 0)]
        pass
    
    def move(self):
        if self.x % self.cell_size == 0 and self.y % self.cell_size == 0:
            self.dx, self.dy = self.next_dir
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        self.start = (self.x, self.y)
        self.x = max(0, min(self.x, 680 - self.width))
        self.y = max(0, min(self.y, 600 - self.height))
        
        
        self.orient()
    def orient(self):
        if self.dx == 1:
            self.head = pygame.transform.rotate(self.original, 270)
        elif self.dx == -1:
            self.head = pygame.transform.rotate(self.original, 90)
        elif self.dy == 1:
            self.head = pygame.transform.rotate(self.original, 180)
        elif self.dy == -1:
            self.head = self.original
        pass