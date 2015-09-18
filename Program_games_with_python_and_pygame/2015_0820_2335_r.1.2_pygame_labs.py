import pygame
import random
pygame.init()

## define some colors
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
# set the width and height of hte screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

class Rectangle():
    x = 0
    y = 0
    height = 0
    width = 0
    change_x = 2
    change_y = 4
    def draw(self, screen):
        color = rand_color()
        pygame.draw.rect(screen, color, [self.x, self.y, self.height, self.width])
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

class Ellipse(Rectangle):
    def draw(self, screen):
        pygame.draw.ellipse(screen, (255,0,255), [self.x, self.y, self.height, self.width])
#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []
for n in range(1000):
    my_object = Rectangle()
    my_object.color = rand_color
    my_object.x = random.randint(0, 700)
    my_object.y = random.randint(0, 500)
    my_object.height = random.randint(20,70)
    my_object.width = random.randint(20,70)
    my_object.change_x = random.randint(-3, 3)
    my_object.change_y = random.randint(-3, 3)
    my_list.append(my_object)
for n in range(1000):
    my_object = Ellipse()
    my_object.color = rand_color
    my_object.x = random.randint(0, 700)
    my_object.y = random.randint(0, 500)
    my_object.height = random.randint(20,70)
    my_object.width = random.randint(20,70)
    my_object.change_x = random.randint(-3, 3)
    my_object.change_y = random.randint(-3, 3)
    my_list.append(my_object)

#------Main Program Loop-------#
while not done:
    #-- main event loop --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- Game logic should go here -- #

    # -- Drawing code should go here -- #
    screen.fill(white)
    for item in my_list:
        item.draw(screen)
        item.move()


    pygame.display.flip()
    # -- Limit to 60 frames per second -- #
    clock.tick(60)
pygame.quit()
