import pygame
pygame.init()
win =pygame.display.set_mode([500,480])
pygame.display.set_caption("first game")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,height,width):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left =False
        self.right=False
        self.walkcount=0
        self.standing =True
        self.hitbox =(self.x+17,self.y+11,29,52)

    def draw(self, win):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1
            elif self.right:
                win.blit(walkRight[self.walkcount//3], (self.x,self.y))
                self.walkcount +=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox=(self.x+17,self.y+11,29,52)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)

class projectile(object):
    def __init__ (self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing 
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
        # define the player and the projectiles


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end=end 
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox=(self.x+10,self.y+2,31,57)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        self.hitbox=(self.x+10,self.y+2,31,57)

        pygame.draw.rect(win,(255,0,0),self.hitbox,2)    
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
                                   
    def hit(self):
        print('hit')

def redrawgamewindow():
    win.blit(bg ,(0,0))
    nithin.draw(win)
    sandhya.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# main loop
nithin = player(200,410,64,64) 
sandhya= enemy(100,410,64,64,300)
shoot=0
running = True
bullets =[]
while running:
    clock.tick(27)
    if shoot >0 :
        shoot+=1
    if shoot>3:
        shoot=0    
    for event in pygame.event.get():
    # to check for event(events are everything we do on console example moving mouse)
        if event.type == pygame.QUIT:
        # providing exit button on window 
            running = False
    for bullet in bullets:
        if bullet.y - bullet.radius <sandhya.hitbox[1] +sandhya.hitbox[3] and bullet.y +bullet.radius >sandhya.hitbox[1]:
            if bullet.x +bullet.radius >sandhya.hitbox[0] and bullet.x -bullet.radius <sandhya.hitbox[0]+sandhya.hitbox[2]:
                sandhya.hit()
                bullets.pop(bullets.index(bullet))   
        if bullet.x <500 and bullet.x >0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shoot == 0:
        if nithin.left:
            facing =-1
        else:
            facing =1
        if len(bullets) <5:
            bullets.append(projectile(round(nithin.x + nithin.width //2),round(nithin.y + nithin.height//2),6,(0,0,0),facing))
        shoot = 1
    if keys[pygame.K_LEFT] and nithin.x >nithin.vel:
        nithin.x -= nithin.vel
        nithin.left =True
        nithin.right =False
        nithin.standing =False
         #to move left we will substract from the x axis
    elif keys[pygame.K_RIGHT] and nithin.x < 500 -nithin.width -nithin.vel:
        # this and condition will prevent character from moving off screen
        nithin.x += nithin.vel #to move right we will add
        nithin.right= True
        nithin.left =False
        nithin.standing =False
    else:
        nithin.standing =True
        nithin.walkcount = 0
    if not(nithin.isJump):
            if keys[pygame.K_UP]:
                nithin.isJump =True
                nithin.right =False
                nithin.left =False
                nithin.walkcount =0
    else:
        if nithin.jumpCount >= -10:
            neg =1
            if nithin.jumpCount <0:
                neg =-1
            nithin.y -= (nithin.jumpCount **2)*0.5*neg
            nithin.jumpCount -=1
        else:
            nithin.isJump =False
            nithin.jumpCount =10
    redrawgamewindow()
pygame.quit()