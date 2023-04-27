import pygame
from pygame.locals import *
import random
import sys

# All the functions related to the game logic and user interface

def show_start_screen(screen, width, height):
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

def show_end_screen(screen, width, height):
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


def draw_background(screen, width, height, road_width, roadmark_width):
    screen.fill((180, 150, 50))
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_width / 2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_width / 2 + roadmark_width * 2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_width / 2 - roadmark_width * 3, 0, roadmark_width, height))


def draw_level(level,screen):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

def respawn_enemy_car(left_lane, right_lane):
    lane = random.choice([left_lane, right_lane])
    y = -200
    return (lane, y)

def draw_level_info(screen, level, width):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(text, (width - 100, 10))
