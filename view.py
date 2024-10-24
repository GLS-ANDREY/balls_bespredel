import pygame

import model


pygame.init()
font = pygame.font.SysFont("arial", 20, True)

display = pygame.display.set_mode([750, 750])
pygame.display.set_caption("Шариковый беспредел")

def risovanie():
    global y_nadpisi
    y_nadpisi = 0
    display.fill([0, 0, 0])
    all_nadpisi = [
        "Esc - Скрыть/показать детали",

        "Шариков в секунду:" + str(model.sharik_per_second)
    ]

    for all_nadpisi_zapis in all_nadpisi:
        all_nadpisi_render = font.render(all_nadpisi_zapis,True,[255,255,255])
        all_nadpisi_render.convert_alpha()
        all_nadpisi_render.set_alpha(model.alpha)
        display.blit(all_nadpisi_render,[0,y_nadpisi])
        y_nadpisi += 25

    pygame.display.flip()