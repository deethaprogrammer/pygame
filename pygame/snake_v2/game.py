import pygame
from screen_and_menu import Menu

move_delay = 30

last_move_time = pygame.time.get_ticks()

pygame.init()
menu = Menu()

clock = pygame.time.Clock()
menu.Screen()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if menu.GameMode == 0:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        menu.GameMode = 1
                    elif event.key == pygame.K_2:
                        menu.GameMode = 2
                        menu.Screen()
                    
            if any(rect.collidepoint(mouse_pos) for rect in menu.rects):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if any(rect.collidepoint(mouse_pos) for rect in menu.rects):
                    if menu.rect_play.collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        menu.GameMode = 1
                    if menu.rect_option.collidepoint(mouse_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        menu.GameMode = 2
                        menu.Screen()
        
        if menu.GameMode == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not (menu.snake.dy == 1):
                    menu.snake.next_dir = 0, -1
                if event.key == pygame.K_s and not (menu.snake.dy == -1):
                    menu.snake.next_dir = 0, 1
                if event.key == pygame.K_a and not (menu.snake.dx == 1):
                    menu.snake.next_dir = -1, 0
                if event.key == pygame.K_d and not (menu.snake.dx == -1):
                    menu.snake.next_dir = 1, 0
                    
        if menu.GameMode == 2:
            mouse_pos = pygame.mouse.get_pos()
            if any(rect.collidepoint(mouse_pos) for rect in menu.snake_rects):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(menu.snake_rects):
                    if rect.collidepoint(mouse_pos):
                        menu.snake.head = menu.option.snake[i]
                        menu.snake.original = menu.option.snake[i]
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.GameMode = 0
    menu.Screen()
    if menu.GameMode == 1:
        now = pygame.time.get_ticks()
        if now - last_move_time > move_delay:
            menu.runner.move()
            last_move_time = now

    pygame.display.update()
    clock.tick(120)
pygame.quit()