import pygame


def allsobitiya():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.QUIT:
            exit()
