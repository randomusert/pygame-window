import pygame
pygame.init()
screen = pygame.display.set_mode([300,450])
pygame.display.set_caption('hello')
running = True
def window():
    while running:
        while running:
           for event in pygame.event.get():
             if event == (pygame.QUIT):
                running = False
                screen.fill(255,165,0)
        pygame.display.flip()
    pygame.quit()