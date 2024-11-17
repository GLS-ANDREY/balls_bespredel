import pygame,model,random

pygame.key.set_repeat(10)
slovari = pygame.event.custom_type()


def allsobitiya():
    global slovari
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.QUIT:
            exit()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_ESCAPE:
            model.visible_settings = not model.visible_settings

        if a.type == pygame.KEYDOWN and a.key == pygame.K_UP:
            model.sharik_per_second += 1
            pygame.time.set_timer(slovari, int(1000 / model.sharik_per_second))

        if a.type == pygame.KEYDOWN and a.key == pygame.K_DOWN and model.sharik_per_second >= 1:
            model.sharik_per_second -= 1
            if model.sharik_per_second != 0:
                pygame.time.set_timer(slovari, int(1000 / model.sharik_per_second))

        if  model.sharik_per_second >= 1 and a.type == slovari:
            sharik = {"color": [random.randint(50, 230), random.randint(50, 230), random.randint(50, 230)],
                      "coord": [random.randint(30, 700), random.randint(30, 700)], "radius": random.randint(5, 20)}
            model.all_sharik.append(sharik)

        if a.type == pygame.KEYDOWN and a.key == pygame.K_DELETE:
            model.all_sharik.clear()


