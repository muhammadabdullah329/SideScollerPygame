# importing the pygame module
import pygame
import random
import os
import time

# initialize the pygame module
pygame.init()
# load and set the logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Running Jack")

# screen size
WIDTH = 800
HEIGHT = 600

# colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# create a surface on screen that has the size of 600 x 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#load images in program
runAnimation = [pygame.image.load(os.path.join("player_img", "run1.png")), pygame.image.load(os.path.join("player_img", "run2.png")),
                pygame.image.load(os.path.join("player_img", "run3.png")), pygame.image.load(os.path.join("player_img", "run4.png")),
                pygame.image.load(os.path.join("player_img", "run5.png")), pygame.image.load(os.path.join("player_img", "run6.png")),
                pygame.image.load(os.path.join("player_img", "run7.png")), pygame.image.load(os.path.join("player_img", "run8.png"))]

backgroundIMG = pygame.image.load("bg.png")
car = pygame.image.load("car.png")

# define a variable to control the main loop
running = True

scorefont = pygame.font.SysFont("monospace",32)
# obstacle Position variables
OX = 800
OY = 280
speed = 7
CLOCK = pygame.time.Clock()

# background speed
BX= 800

# score variable
score = 0

def collision():
    if (180 >= OX >= 100) or (180 >= OX+200 >= 100):
        if character.y >= 275:
            screen.blit(scorefont.render("You Lose!",1,BLACK),(325,250))
            return False

# player object
class Character:
    # person position variables
    x = 100
    y = 300
    jump = False
    comedown = False
    runcount = 0.5
    vel=5

    def jumpFunc(self):
        # Jumping Mechanism
        if self.jump is True:
            self.y -= self.vel
            if self.y <= 120:
                self.jump = False

        if self.jump is False and self.y <= 120:
            self.comedown = True

        if self.comedown is True:
            self.y += self.vel
            if self.y >= 300:
                self.comedown = False

    def draw(self):
        screen.blit(runAnimation[round(self.runcount % 7)], (self.x, self.y))
        self.runcount += 0.13

# surface,color,rectangle [x y width height]
#pygame.draw.rect(screen, BLUE, [self.x, self.y, 20, 50])


character = Character()
firsttime = True
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

        # character movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and character.y >= 300:
                character.jump = True


    character.jumpFunc()
    # background moving mechanism
    BX -= 5
    if BX < 0:
        BX = 800
    # obstacle moving mechanism
    OX -= speed
    if OX < -250:
        OX = 800
        score += 1

    # difficulty level
    if 12 > score > 5:
        speed = 10
        character.vel = 7
    if score > 12:
        speed = random.randrange(10, 18)

    # screen background color and images
    screen.fill(WHITE)
    screen.blit(backgroundIMG, (BX, 0))
    screen.blit(backgroundIMG, (BX-800, 0))

    # all display draw calls
    text=scorefont.render("Score: %d"%score,1,BLACK)
    screen.blit(text,(10,10))
    character.draw()
    screen.blit(car, (OX, OY))

    # detecting collision
    if collision() is False:
        running = False

    # FPS
    CLOCK.tick(60)
    # whole screen updating
    pygame.display.update()
    if firsttime is True:
        time.sleep(1)
        firsttime = False

time.sleep(1)
pygame.quit()
quit()
