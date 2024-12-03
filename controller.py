import pygame, model, random

pygame.key.set_repeat(10)
slovari = pygame.event.custom_type()

speed_ball = pygame.event.custom_type()
pygame.time.set_timer(speed_ball, 10)

def allsobitiya():
    global slovari
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()

        if a.type == pygame.MOUSEMOTION:
            model.prizhok_x = a.pos[0]

        if a.type == speed_ball and model.mode == False:
            model.dvizhenie_sharov()
            model.otbivka_sharov()

        if a.type == pygame.KEYUP and a.key == pygame.K_ESCAPE:
            model.visible_settings = not model.visible_settings

        if a.type == pygame.KEYDOWN and a.key == pygame.K_UP:
            model.sharik_per_second += 1
            pygame.time.set_timer(slovari, int(1000 / model.sharik_per_second))

        if a.type == pygame.KEYDOWN and a.key == pygame.K_DOWN and model.sharik_per_second >= 1:
            model.sharik_per_second -= 1
            if model.sharik_per_second != 0:
                pygame.time.set_timer(slovari, int(1000 / model.sharik_per_second))

        if model.sharik_per_second >= 1 and a.type == slovari:
            sharik = {"color": [random.randint(50, 230), random.randint(50, 230), random.randint(50, 230)],
                      "coord": [random.randint(20, 700), random.randint(20, 700)], "radius": random.randint(5, 20),
                      "speedx": random.randint(1,5),"speedy": random.randint(1,5),"speedy_padenie": 0}
            model.all_sharik.append(sharik)

        if a.type == pygame.KEYDOWN and a.key == pygame.K_1:
            model.mode = True

        if a.type == speed_ball and model.mode == True:
            model.padenie_sharov()

        if a.type == pygame.KEYDOWN and a.key == pygame.K_DELETE:
            model.all_sharik.clear()
