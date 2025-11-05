import os
import pygame
import json
try:
    from classes_snake import Snake, Food
except Exception as e:
    print("Import failed:", e)
    


pygame.init()
pygame.font.init()
width = 900
height = 900


def save_scores():
    with open(highscores, "w") as file:
        json.dump(highscore, file, indent=4)


screen = pygame.display.set_mode((width, height))

base_path = os.path.dirname(__file__)
img_path = os.path.join(base_path, "assets")

filename = "highscore.json"
highscores = os.path.join(base_path, filename)
if os.path.exists(highscores):
    with open(highscores, "r") as file:
        highscore = json.load(file)
else:
    highscore = {}

head_img = pygame.image.load(os.path.join(img_path, "SNAKE.png")).convert_alpha()
head_img = pygame.transform.scale(head_img, (30, 30))

aple_img = pygame.image.load(os.path.join(img_path, "apple.png")).convert_alpha()
aple_img = pygame.transform.scale(aple_img, (30, 30))
clock = pygame.time.Clock()
MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 100) #time till moving in ms

top_bar_height= 60
score = 0

font = pygame.font.SysFont("Arial", 40)

pygame.display.set_caption("snake")

player = Snake((390, 450, 30, 30))

food = Food((30, 30, width, height))

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

player.next_dir = (player.dx, player.dy)
game_mode = None
def draw_start():
    screen.fill((0,0,0))
    title = font.render("Choose Game Mode", True, (255, 255, 255))
    border_btn = font.render("1: Border Mode", True, (200, 200, 200))
    wrap_btn = font.render("2: Wrap Mode", True, (200, 200, 200))
    chaos_btn = font.render("3: chaos mode", True, (200, 200, 200))
    screen.blit(title, (width//2 - title.get_width()//2, 200))
    screen.blit(border_btn, (width//2 - border_btn.get_width()//2, 300))
    screen.blit(wrap_btn, (width//2 - wrap_btn.get_width()//2, 400))
    screen.blit(chaos_btn, (width//2 - chaos_btn.get_width()//2, 500))
    pygame.display.update()

waiting = True
run = True
while run:
    while waiting:
        draw_start()
        amount_of_food = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = 'border'
                    waiting = False
                elif event.key == pygame.K_2:
                    game_mode = 'wrap'
                    waiting = False
                elif event.key == pygame.K_3:
                    game_mode = 'chaos'
                    amount_of_food = 200
                    waiting = False
                    
        score = 0
        player = Snake((390, 450, 30, 30))
        foods = []
        occupied = player.body.copy()
        for _ in range(amount_of_food):
            food = Food((30, 30, width, height), aple_img)
            food.respawn(width, height, occupied)
            foods.append(food)
            occupied.append((food.x, food.y))  # Add fruit position to avoid overlap
        start_run = True

    text_surface = font.render(f"Game Over! your score was: {score}", True, (255, 255, 255))  # White text
    pygame.draw.rect(screen, (30, 30, 30), (0, 0, width, 60))  # Dark bar
    score_text = font.render(f"Score: {score}  |  highscore: {highscore[game_mode]}", True, (255, 255, 255))
    screen.blit(score_text, (20, 10))
    clock.tick(60)
    TILE_SIZE = 30
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

    food_rect = []
    for food in foods:
        if food.image:
            screen.blit(food.image, (food.x, food.y))
        else:
            pygame.draw.rect(screen, (0, 250, 0), (food.x, food.y, food.size_width, food.size_height))
        food_rect.append(pygame.Rect(food.x, food.y, food.size_width, food.size_height))
    
    head_rect = pygame.Rect(player.body[0][0], player.body[0][1], player.width, player.height)
    
    for i, food_rec in enumerate(food_rect):
        if head_rect.colliderect(food_rec):
            # Prevent overlap with other fruits
            occupied = player.body + [(f.x, f.y) for f in foods]
            foods[i].respawn(width, height, occupied)
            player.eaten()
            score += 1
            if score > highscore[game_mode]:
                highscore[game_mode] = score
            break  # Only eat one fruit per frame
    
        

    if start_run and (player.dx != 0 or player.dy != 0):
        player.eaten()
        start_run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:

            current_dir = (player.dx, player.dy)
            if event.key == pygame.K_w and current_dir != (0, 1):
                player.next_dir = 0, -1
            elif event.key == pygame.K_a and current_dir != (1, 0):
                player.next_dir = -1, 0
            elif event.key == pygame.K_d and current_dir != (-1, 0):
                player.next_dir = 1, 0
            elif event.key == pygame.K_s and current_dir != (0, -1):
                player.next_dir = 0, 1
                
        elif event.type == MOVE_EVENT:
            player.dx, player.dy = player.next_dir
            player.move_ip(game_mode)
            if player.check_self_collision():
                text_rect = text_surface.get_rect(center=(width // 2, (height-200) // 2))
                screen.blit(text_surface, text_rect)
                pygame.display.update()
                pygame.time.wait(3000)
                waiting = True


    pygame.display.update()
save_scores()
pygame.quit()