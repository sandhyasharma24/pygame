import pygame
# to install pygame type" pip install pygame"
# to check if pygame is installed type "pip show pygame"
# pygame is a third party module it is use to make games using python
pygame.init()
# to initialize pygame

win = pygame.display.set_mode([500, 500])
# to create a window

pygame.display.set_caption("First Game")
# to give proper name to window +
x= 50
y =50
# coordinates are the from top left corner
vel= 40
height = 30
width =30
# attributes of character

running = True
while running:
    pygame.time.delay(100) #to set motion time for character
# main loop to check collisions or if you hit something
    for event in pygame.event.get():
    # to check for event(events are everything we do on console example moving mouse)
        if event.type == pygame.QUIT:
        # providing exit button on window 
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel #to move left we will substract from the x axis
    if keys[pygame.K_RIGHT]:
        x += vel #to move right we will add
    if keys[pygame.K_DOWN]: 
        y += vel# to move up and down we will use y-axis
    if keys[pygame.K_UP]: 
        y-= vel
# this conditions will help us in moving character but right now it will only show a train of red rect moving along the screen 
# but we want only out shape to move so to fill its train along with backgroung we will use
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    # to draw shapes on window
    # we put win in parameter to draw shapes on the windows suface
    # given 255,0,0 is color code provide to shape
    # x,y are the coordinates of the shape
    # width and height are the attributes of shape
    pygame.display.update()
    # to update the window with characte or else it wonts show anyhthing


pygame.quit()