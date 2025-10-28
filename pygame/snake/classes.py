import random

class Snake(object):
    def __init__(self, pos):
        x, y, width, height = pos
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 40
        
        self.dx = 0
        self.dy = 0
        
        self.body = [(x, y)]
        
        self.ate = False
    
    def move_ip(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        self.x = max(0, min(self.x, 800 - self.width))
        self.y = max(60, min(self.y, 800 - self.height))
        
        new_head = (self.x, self.y)
        self.body.insert(0, new_head)
        
        if not self.ate:
            self.body.pop()
        else:
            self.ate = False
            
    def eaten(self):
        self.ate = True
        
    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]

        
        
class Food(object):
    def __init__(Item, pos):
        item_width, item_height, screen_width, screen_height = pos
        Item.size_width = item_width
        Item.size_height = item_height
        Item.respawn(screen_width, screen_height, [])
        
    def respawn(Item, screen_width, screen_height, player_body):
        Tile_Size = Item.size_width
        max_x = screen_width // Tile_Size
        max_y = screen_height // Tile_Size
        
        all_positions = [(x * Tile_Size, y * Tile_Size) for x in range(max_x) for y in range(60 // Tile_Size, max_y)]
        valid_position = [pos for pos in all_positions if pos not in player_body]
        if valid_position:
            Item.x, Item.y = random.choice(valid_position)
        else:
            Item.x, Item.y = 0, 60