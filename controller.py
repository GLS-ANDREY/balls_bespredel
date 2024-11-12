import pygame,model,random

def allsobitiya():
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.QUIT:
            exit()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_ESCAPE:
            model.visible_settings = not model.visible_settings
        if a.type == pygame.KEYDOWN and a.key == pygame.K_UP:
            sharik = {"color": [random.randint(50, 230), random.randint(50, 230), random.randint(50, 230)],
                      "coord": [random.randint(30, 700), random.randint(30, 700)], "radius": random.randint(5, 20)}
            model.all_sharik.append(sharik)
        if a.type == pygame.KEYDOWN and a.key == pygame.K_DELETE:
            model.all_sharik.clear()


