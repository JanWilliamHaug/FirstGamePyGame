import pygame
from pygame.locals import *
import random

# shape parameters
size = width, height = (800, 600)
road_width = int(width/1.6)
roadmark_width = int(width/80)

# location parameters
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4

# animation parameters
speed = 1

# initiallize the app
pygame.init()
running = True

# sets window size
screen = pygame.display.set_mode((size))

# sets background color
screen.fill((180,150,50))

# sets title
pygame.display.set_caption("William's car game")


# apply changes
pygame.display.update()

# load player car
car = pygame.image.load("yellowCar.png")
# rezise image
#car = pygame.transform.scale(car, (250, 250))

car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load enemy car
carEnemy = pygame.image.load("whiteCar.png")
carEnemy_loc = car.get_rect()
carEnemy_loc.center = left_lane, height*0.2

level = 0
counter = 0
# game loop
while running:

    # increase game difficulty overtime
    if counter == 5000:
        speed += 0.15
        counter = 0
        level += 1
        print("level up", speed)
        print("Your level is now " + str(level))

    # animate enemy vehicle
    carEnemy_loc[1] += speed
    if carEnemy_loc[1] > height:
        # randomly select lane
        if random.randint(0,1) == 0:
            carEnemy_loc.center = right_lane, -200
        else:
            carEnemy_loc.center = left_lane, -200


    # End game
    if car_loc[0] == carEnemy_loc[0] and carEnemy_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break
    
    
    #event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running = False

        if event.type == KEYDOWN:
            # move user car to the left
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_width/2), 0])
            # move user car to the right
            if event.key in [K_d, K_RIGHT]:
                 car_loc = car_loc.move([int(road_width/2), 0])
                 
                 
    #draw graphics
    #Draws the road as grey
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_width/2, 0, road_width, height))

    #Draw line in the middle of the road
    pygame.draw.rect(
        screen, 
        (255, 240, 60),
        (width/2-roadmark_width/2, 0, roadmark_width, height)
    )


    #Draw white line on the left side of the road
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        (width/2-road_width/2 + roadmark_width*2, 0, roadmark_width, height)
    )

    #Draw white line on the right side
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        (width/2 + road_width/2 - roadmark_width*3, 0, roadmark_width, height)
    )

     # place car images on the screen           
    screen.blit(car, car_loc)
    screen.blit(carEnemy, carEnemy_loc)
    
    # apply changes
    pygame.display.update()

pygame.quit()

