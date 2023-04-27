import pygame
from pygame.locals import *
import random

# Constants related to the game objects
size = width, height = (800, 600)
road_width = int(width / 1.6)
roadmark_width = int(width / 80)
right_lane = width / 2 + road_width / 4
left_lane = width / 2 - road_width / 4

class Car:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("yellowCar.png")
        self.loc = self.image.get_rect()
        self.loc.center = x, y

    def draw(self):
        self.screen.blit(self.image, self.loc)

    def handle_input(self, event, road_width):
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                new_car_loc = self.loc.move([-int(road_width / 2), 0])
                if new_car_loc[0] >= width / 2 - road_width / 2:
                    self.loc = new_car_loc
            if event.key in [K_d, K_RIGHT]:
                new_car_loc = self.loc.move([int(road_width / 2), 0])
                if new_car_loc[0] <= width / 2 + road_width / 2 - self.image.get_width():
                    self.loc = new_car_loc

    def check_collision(self, enemy_car):
        return self.loc[0] == enemy_car.loc[0] and enemy_car.loc[1] > self.loc[1] - 250

class EnemyCar:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("whiteCar.png")
        self.loc = self.image.get_rect()
        self.loc.center = x, y

    def draw(self):
        self.screen.blit(self.image, self.loc)

    def update(self, speed, height, left_lane, right_lane):
        self.loc[1] += speed
        if self.loc[1] > height:
            if random.randint(0, 1) == 0:
                self.loc.center = right_lane, -200
            else:
                self.loc.center = left_lane, -200
