#snake.py
import pygame

class Snake:
    def __init__(self, snake_head):
        self.original = snake_head
        self.head = pygame.transform.rotate(snake_head, 90)
        self.width = 40
        self.height = 40
        self.speed = 40
        self.x = 160
        self.y = 320
        self.start = (self.x, self.y)
        self.dx = 0
        self.dy = 0
        self.next_dir = (0, 0)
        self.cell_size = 40
        self.history = []
        self.body_lenght = 0
        self.segment_spacing = 2
        self.body_color = (0, 200, 0)   # bright green block
        self.aligned_this_frame = False

        
    
    def move(self):
    # reset flag every frame
        self.aligned_this_frame = False

        # Only update direction + body when aligned to grid (BEFORE moving)
        if self.x % self.cell_size == 0 and self.y % self.cell_size == 0:
            self.dx, self.dy = self.next_dir

            # Record grid position for body
            self.history.insert(0, (self.x, self.y))

            # Trim history
            if len(self.history) > self.body_lenght + 5:
                self.history.pop()

            # we updated body on a grid tile this frame
            self.aligned_this_frame = True

        # Smooth movement every frame
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        self.x = max(0, min(self.x, 680 - self.width))
        self.y = max(0, min(self.y, 600 - self.height))
        self.start = (self.x, self.y)

        self.body = self.history[:self.body_lenght]
        if (self.x, self.y) in self.body:
            score = self.body_lenght
            print(f"GAME OVER YOUR SCORE WAS: {score}")
            quit()

        self.orient()
    
    def grow(self):
        self.body_lenght += 1
    
    def orient(self):
        if self.next_dir == (1, 0):
            self.head = pygame.transform.rotate(self.original, 90)
        elif self.next_dir == (-1, 0):
            self.head = pygame.transform.rotate(self.original, 270)
        elif self.next_dir == (0, 1):
            self.head = self.original
        elif self.next_dir == (0, -1):
            self.head = pygame.transform.rotate(self.original, 180)
        elif self.next_dir == (-1, -1):
            self.head = pygame.transform.rotate(self.original, 225)
        elif self.next_dir == (1, -1):
            self.head = pygame.transform.rotate(self.original, 135)
        elif self.next_dir == (-1, 1):
            self.head = pygame.transform.rotate(self.original, 315)
        elif self.next_dir == (1, 1):
            self.head = pygame.transform.rotate(self.original, 45)