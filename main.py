import pygame
from pygame.locals import *
import sys

from game_objects import Car, EnemyCar, road_width, roadmark_width, left_lane, right_lane
from game_functions import show_start_screen, show_end_screen, draw_background, draw_level_info, respawn_enemy_car

# Initialize Pygame and set up display
pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode((size))
screen.fill((180, 150, 50))
pygame.display.set_caption("William's car game")
pygame.display.update()

# Load game objects
player_car = Car(screen, right_lane, height * 0.8)
enemy_car = EnemyCar(screen, left_lane, height * 0.2)

# Set initial game state
level = 1
counter = 0
speed = 1

while True:
    # Show start screen and wait for user input
    show_start_screen(screen, width, height)
    draw_background(screen, width, height, road_width, roadmark_width)
    running = True
    enemy_car.loc.center = respawn_enemy_car(left_lane, right_lane)

    # Main game loop
    while running:
        counter += 1
        draw_level_info(screen, level, width)

        # Level up every 3000 frames
        if counter == 3000:
            speed += 0.15
            counter = 0
            level += 1
            print("level up")
            print("You are now level " + str(level))

        # Update enemy car location
        enemy_car.update(speed, height, left_lane, right_lane)

        # Check for collisions
        if player_car.check_collision(enemy_car):
            running = False
            break

        # Handle user input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            player_car.handle_input(event, road_width)

        # Draw game objects and update the display
        draw_background(screen, width, height, road_width, roadmark_width)
        draw_level_info(screen, level, width)
        player_car.draw()
        enemy_car.draw()
        pygame.display.update()

    # Show end screen and wait for user input
    if not show_end_screen(screen, width, height):
        break

    # Reset game state for a new game
    running = True
    level = 1
    speed = 1
    counter = 0
    enemy_car.loc.center = respawn_enemy_car(left_lane, right_lane)

pygame.quit()
