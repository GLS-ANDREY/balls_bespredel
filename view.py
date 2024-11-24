import pygame, model, random

pygame.init()
font = pygame.font.SysFont("arial", 20, True)

display = pygame.display.set_mode([750, 750])
pygame.display.set_caption("Шариковый беспредел")


def risovanie():
    global y_nadpisi
    y_nadpisi = 0
    display.fill([0, 0, 0])

    for infa_sharik in model.all_sharik:
        pygame.draw.circle(display, infa_sharik["color"], infa_sharik["coord"], infa_sharik["radius"])

    if model.visible_settings == True:
        all_nadpisi = [
            "Esc - Скрыть/показать детали",
            "Вверх - +шарики в секунду",
            "Вниз - -шарики в секунду",
            "Del - Удалить все шарики",
            "Шариков в секунду:" + str(model.sharik_per_second),
            "Всего шариков:" + str(len(model.all_sharik))
        ]

        for all_nadpisi_zapis in all_nadpisi:
            all_nadpisi_render = font.render(all_nadpisi_zapis, True, [255, 255, 255])
            all_nadpisi_render.convert_alpha()
            all_nadpisi_render.set_alpha(model.alpha)
            display.blit(all_nadpisi_render, [0, y_nadpisi])
            y_nadpisi += 25

    pygame.display.flip()
