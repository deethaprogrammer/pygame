import os
import pygame
try:
    from classes import Snake, Food
except Exception as e:
    print("Import failed:", e)

pygame.init()
pygame.font.init()

width = 800
height = 1000

screen = pygame.display.set_mode((width, height))

base_path = os.path.dirname(__file__)
img_path = os.path.join(base_path, "assets", "SNAKE.png")

head_img = pygame.image.load(img_path).convert_alpha()
head_img = pygame.transform.scale(head_img, (40, 40))

clock = pygame.time.Clock()
MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 100) #time till moving in ms

top_bar_height= 60
font = pygame.font.SysFont("Arial", 40)
text_surface = font.render("Game Over!", True, (255, 255, 255))  # White text

pygame.display.set_caption("snake")

player = Snake((400, 400 + top_bar_height, 40, 40))

food = Food((40, 40, width, height))

start_run = True

def get_rotation(dx, dy, head_img):
    if dx == 1:
        
        return pygame.transform.rotate(head_img, 270)
    elif dx == -1:
        
        return pygame.transform.rotate(head_img, 90)
    elif dy == -1:
        
        return head_img
    elif dy == 1:
        
        return pygame.transform.rotate(head_img, 180)
    return head_img


score = 0
run = True
while run:
    pygame.draw.rect(screen, (30, 30, 30), (0, 0, width, 60))  # Dark bar
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 10))
    clock.tick(60)
    TILE_SIZE = 40
    for x in range(0, width, TILE_SIZE):
        for y in range(top_bar_height, height, TILE_SIZE):
            color = (50, 50, 50) if (x // TILE_SIZE + y // TILE_SIZE) % 2 == 0 else (60, 60, 60)
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)
            
    for i, segment in enumerate(player.body):
        if i == 0:
            rotated_head = get_rotation(player.dx, player.dy, head_img)
            screen.blit(rotated_head, (segment[0], segment[1]))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (segment[0], segment[1], player.width, player.height))

    food_rect = pygame.draw.rect(screen, (0, 250, 0), (food.x, food.y, food.size_width, food.size_height))
    
    head_rect = pygame.Rect(player.body[0][0], player.body[0][1], player.width, player.height)
    
    if head_rect.colliderect(food_rect):
        food.respawn(width, height-200, player.body)
        player.eaten()
        score += 1
    
        

    if start_run and (player.dx != 0 or player.dy != 0):
        player.eaten()
        start_run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:

            current_dir = (player.dx, player.dy)
            if event.key == pygame.K_w and current_dir != (0, 1):
                player.dx, player.dy = 0, -1
            elif event.key == pygame.K_a and current_dir != (1, 0):
                player.dx, player.dy = -1, 0
            elif event.key == pygame.K_d and current_dir != (-1, 0):
                player.dx, player.dy = 1, 0
            elif event.key == pygame.K_s and current_dir != (0, -1):
                player.dx, player.dy = 0, 1
        elif event.type == MOVE_EVENT:
            player.move_ip()
            if player.check_self_collision():
                text_rect = text_surface.get_rect(center=(width // 2, (height-200) // 2))
                screen.blit(text_surface, text_rect)
                pygame.display.update()
                pygame.time.wait(3000)
                run = False


    pygame.display.update()

pygame.quit()