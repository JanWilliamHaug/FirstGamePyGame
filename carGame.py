import pygame
from pygame.locals import *
import random
import sys


def show_start_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Are you ready? Press Enter to start the game!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width / 2, height / 3))
    screen.blit(text, text_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return
        pygame.time.delay(100)


def show_end_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("GAME OVER! YOU LOST!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width / 2, height / 2))
    screen.blit(text, text_rect)

    subtext = font.render("Press 'R' to restart or 'Q' to quit", True, (0, 0, 0))
    subtext_rect = subtext.get_rect(center=(width / 2, height / 2 + 50))
    screen.blit(subtext, subtext_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    return True
                if event.key == K_q:
                    return False
        pygame.time.delay(100)


def draw_background():
    screen.fill((180, 150, 50))
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_width / 2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_width / 2 + roadmark_width * 2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_width / 2 - roadmark_width * 3, 0, roadmark_width, height))


def draw_level(level):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

def respawn_enemy_car():
    lane = random.choice([left_lane, right_lane])
    y = -200
    return (lane, y)

def draw_level_info(level):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(text, (width - 100, 10))



size = width, height = (800, 600)
road_width = int(width / 1.6)
roadmark_width = int(width / 80)
right_lane = width / 2 + road_width / 4
left_lane = width / 2 - road_width / 4
speed = 1

pygame.init()
screen = pygame.display.set_mode((size))
screen.fill((180, 150, 50))
pygame.display.set_caption("William's car game")
pygame.display.update()

car = pygame.image.load("yellowCar.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

carEnemy = pygame.image.load("whiteCar.png")
carEnemy_loc = carEnemy.get_rect()
carEnemy_loc.center = left_lane, height * 0.2

level = 1
counter = 0

while True:
    show_start_screen()
    draw_background()
    running = True
    carEnemy_loc.center = respawn_enemy_car()


    while running:
        counter += 1
        draw_level(level)

        if counter == 3000:
            speed += 0.15
            counter = 0
            level += 1
            print("level up")
            print("You are now level " + str(level))

        carEnemy_loc[1] += speed
        if carEnemy_loc[1] > height:
            if random.randint(0, 1) == 0:
                carEnemy_loc.center = right_lane, -200
            else:
                carEnemy_loc.center = left_lane, -200

        if car_loc[0] == carEnemy_loc[0] and carEnemy_loc[1] > car_loc[1] - 250:
            running = False
            break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    new_car_loc = car_loc.move([-int(road_width / 2), 0])
                    if new_car_loc[0] >= width / 2 - road_width / 2:
                        car_loc = new_car_loc
                if event.key in [K_d, K_RIGHT]:
                    new_car_loc = car_loc.move([int(road_width / 2), 0])
                    if new_car_loc[0] <= width / 2 + road_width / 2 - car.get_width():
                        car_loc = new_car_loc

        draw_background()
        draw_level_info(level)
        screen.blit(car, car_loc)
        screen.blit(carEnemy, carEnemy_loc)
        pygame.display.update()

    if not show_end_screen():
        break

    running = True
    level = 1
    speed = 1
    counter = 0
    #carEnemy_loc.center = left_lane, height * 0.2
    carEnemy_loc.center = respawn_enemy_car()

pygame.quit()

