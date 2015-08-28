##create a picture using pygame
import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 255)
YELLOW = (248, 255, 0)
PURPLE = (150, 0, 150)
BLACK_PURPLE = (50, 0, 50)
BLACK_GRAY = (30, 30, 30)
BLUE_PURPLE = (15, 0, 65)
BLACK_BLUE = (0, 0, 50)
BLACK_BIT_O_BLUE = (0, 0, 15)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Israel's Awesome Game")


done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BLACK)
    
    #draw background
    pygame.draw.rect(screen, BLUE_PURPLE, [0, 0, 700, 200])
    pygame.draw.rect(screen, BLACK_BLUE, [0, 175, 700, 75])
    pygame.draw.rect(screen, BLACK_BIT_O_BLUE, [0, 225, 700, 25])

    #draw the moon
    pygame.draw.ellipse(screen, WHITE, [50, 25, 100, 100])

    #draw main building
    pygame.draw.rect(screen, PURPLE, [230,75, 150, 425])
    pygame.draw.polygon(screen, BLACK_PURPLE, [[250, 65], [230, 75], [380, 75], [400, 65]])
    pygame.draw.polygon(screen, BLACK_PURPLE, [[400,65], [380, 75], [380, 500], [400, 500]])
    pygame.draw.line(screen, BLACK_GRAY, [380,75], [400, 65], 1)

    ##draw windows
    window_colum = 250
    window_row = 100
    for i in range(0, 400, 50):
        for i in range(0, 120, 30):
            pygame.draw.rect(screen, BLACK_PURPLE, [window_colum + i, window_row, 15, 25])
        window_row += 50


    pygame.display.flip()

    clock.tick(60)


pygame.quit()
