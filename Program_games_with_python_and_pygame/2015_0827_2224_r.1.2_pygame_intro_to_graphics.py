##create a picture using pygame
import pygame
import random
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

pi = 3.14159265359
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Israel's Awesome Game")
moon_x = -100
moon_y = 195
x_change = 2
y_change = -1
rain = []
background = pygame.image.load("2015_0907_1656_C.3_background_image_night_sky.png").convert()
player_image = pygame.image.load("2015_0907_1704_C.3_player_icon_red_car.png").convert()
player_image.set_colorkey(BLACK)
click_sound = pygame.mixer.Sound('2015_0907_1830_C.3_bomb_sound_effect.wav')
for i in range(50):
    rain_x = random.randrange(0, 700)
    rain_y = random.randrange(0, 500)
    rain.append([rain_x, rain_y])

def draw_building(screen, x, y):
    pygame.draw.rect(screen, PURPLE, [x, y, 150, 425]) #front
    pygame.draw.polygon(screen, BLACK_PURPLE, [[x + 20, y - 10], [x, y], [x + 150, y], [x + 170, y - 10]]) #roof
    pygame.draw.polygon(screen, BLACK_PURPLE, [[x + 170, y - 10], [x + 150, y], [x + 150, y + 425], [x + 170,  y + 425]]) #side
    pygame.draw.line(screen, BLACK_GRAY, [x + 150, y], [x + 170,  y - 10], 1) #right diagonal
    pygame.draw.line(screen, BLACK_GRAY, [x, y], [x,  y + 450], 1)
    window_colum = x + 20
    window_row =  y + 25
    for i in range(0, 400, 50):
        for i in range(0, 120, 30):
            pygame.draw.rect(screen, BLACK_PURPLE, [window_colum + i, window_row, 15, 25])
        window_row += 50

def draw_car(screen, x, y):
    pygame.draw.polygon(screen, WHITE, [[x, y], [x, y + 15],[x + 100, y + 15], [ x + 97, y + 10], [x + 60, y], [x + 55, y - 5],[x + 20, y - 8], [x + 8, y - 1], [x, y]])
    pygame.draw.ellipse(screen, BLACK, [x + 15, y + 9, 14, 14])
    pygame.draw.ellipse(screen, BLACK, [x + 65, y + 9, 14, 14])

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print ("Error, I didn't find any joystick.")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 480
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
    

    if joystick_count != 0:
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)

        x_coord = x_coord + int(horiz_axis_pos * 10)
        y_coord = y_coord + int(vert_axis_pos * 10)       

    x_coord += x_speed
    y_coord += y_speed

    pos = pygame.mouse.get_pos()
    
    screen.fill(BLACK)
    
    #draw background
    #pygame.draw.rect(screen, BLUE_PURPLE, [0, 0, 700, 200])
    #pygame.draw.rect(screen, BLACK_BLUE, [0, 175, 700, 75])
    #pygame.draw.rect(screen, BLACK_BIT_O_BLUE, [0, 225, 700, 25])

    screen.blit(background, [0,0])

    #draw the moon
    pygame.draw.ellipse(screen, WHITE, [moon_x, moon_y, 100, 100])
    if moon_x >= 700:
        moon_x = -100
        moon_y = 195
        y_change *= -1
    else:
        moon_x += x_change
    if moon_y <= -75:
        y_change *= -1
    moon_y += y_change


    ##draw main building
    draw_building(screen, 230,75)
    draw_building(screen, 300, 185)
    draw_building(screen, 150, 200)
    draw_building(screen, 10, 135)
    draw_building(screen, 500, 100)

    #draw car
    #draw_car(screen, pos[0], pos[1])
    player_position = pygame.mouse.get_pos()
    player_x = player_position[0]
    player_y = player_position[1]
   
    screen.blit(player_image, [player_x, player_y])
    draw_car(screen, x_coord, y_coord) 


    #draw and animate the rain
    for item in rain:
        if item[1] > 500:
            item[1] = random.randrange(-20, -5)
        pygame.draw.ellipse(screen, WHITE, [item[0], item[1], 3, 3])
        item[1] += 1


    pygame.display.flip()

    clock.tick(60)


pygame.quit()
