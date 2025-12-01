import pygame
from screen_and_menu import Menu
pygame.init()

menu = Menu()
menu.Screen()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if menu.GameMode is None:
                if event.key == pygame.K_0:
                    print("Yeah")
                    menu.GameMode = '1'
                else:
                    print('Wrong key')
            else:
                print("in Gamemode")
    pygame.display.update()
pygame.quit()