import pygame
from classes import tic_tac
import random

pygame.init()
width = 600
height = 660
font = pygame.font.SysFont(None, 48)
boxfont = pygame.font.SysFont(None, 120)
screen = pygame.display.set_mode((width, height))
symbols = []
run = True
score = {'x': 0, 'O': 0}
box_size = 200
boxes = []
for row in range(3):
    for col in range(3):
        box_x = col * box_size
        box_y = row * box_size + 60
        rect = pygame.Rect(box_x, box_y, box_size, box_size)
        boxes.append({'rect': rect, 'symbol': None, 'row': row, 'col': col})
        
def win_chek(boxes, player):
    grid = [[None for _ in range(3)] for _ in range(3)]
    for box in boxes:
        grid[box['row']][box['col']] = box['symbol']
    for i in range(3):
        if all(grid[i][j] == player for j in range(3)): return True
        if all(grid[j][i] == player for j in range(3)): return True
        
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] == player:
        return True

    
    return False
def draw_start():
    screen.fill((0, 0, 0))
    text_survice = font.render(f"x score: {score['x']}  |  O score: {score['O']}", True, (250, 210, 0))
    screen.blit(text_survice, (10, 20))
    start_btn = font.render("press one to start", True, (200, 200, 200))
    screen.blit(start_btn, (width//2 - start_btn.get_width()//2, 300))
    pygame.display.flip()


start = True  
while run:
    while start:
        draw_start()
        current_player = 'x'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start = False
                    
    screen.fill("grey")
    pygame.draw.rect(screen, (30, 30, 30), (0, 0, 600, 60))
    text_survice = font.render(f"x score: {score['x']}  |  O score: {score['O']}", True, (250, 210, 0))
    screen.blit(text_survice, (10, 20))
    for symbol in symbols:
        symbol.draw(screen, boxfont)           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if current_player == 'x':
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for box in boxes:
                    if box['rect'].collidepoint(pos) and box['symbol'] is None:
                        box['symbol'] = current_player
                        symbols.append(tic_tac(current_player, box['rect'].center))
                        if win_chek(boxes, current_player):
                            score[current_player] += 1
                            for box in boxes:
                                box['symbol'] = None
                                symbols.clear()
                                pygame.display.flip()
                                start = True
                        else:   
                            current_player = 'O'
        elif current_player == 'O':
            random_box = random.choice([box for box in boxes if box['symbol'] is None])
            random_box['symbol'] = current_player
            symbols.append(tic_tac(current_player, random_box['rect'].center))
            if win_chek(boxes, current_player):
                score[current_player] += 1
                for box in boxes:
                    box['symbol'] = None
                    symbols.clear()
                    pygame.display.flip()
                    start = True
            else:   
                current_player = 'x'
    for box in boxes:
        pygame.draw.rect(screen, (100, 100, 100), box['rect'], width=3)
    if all(box['symbol'] is not None for box in boxes):
        for box in boxes:
            box['symbol'] = None
            symbols.clear()
            pygame.display.flip()
            start = True
    pygame.display.flip()
pygame.quit()