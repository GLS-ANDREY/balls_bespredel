import pygame, random

mode = False
all_sharik = []
sharik_per_second = 0
alpha = 180
visible_settings = True


def dvizhenie_sharov():
    for infa_sharik in all_sharik:
        infa_sharik["coord"][0] += infa_sharik["speedx"]
        infa_sharik["coord"][1] += infa_sharik["speedy"]


def otbivka_sharov():
    for infa_sharik in all_sharik:
        if infa_sharik["coord"][1] + infa_sharik["radius"] >= 750:  # низ
            infa_sharik["speedy"] *= -1

        if infa_sharik["coord"][1] - infa_sharik["radius"] <= 0:  # верх
            infa_sharik["speedy"] *= -1

        if infa_sharik["coord"][0] + infa_sharik["radius"] >= 750:  # право
            infa_sharik["speedx"] *= -1

        if infa_sharik["coord"][0] - infa_sharik["radius"] <= 0:  # лево
            infa_sharik["speedx"] *= -1


def padenie_sharov():
    for infa_sharik in all_sharik:
        infa_sharik["coord"][1] += infa_sharik["speedy_padenie"]

        if infa_sharik["coord"][1] >= 750 - infa_sharik["radius"]:
            infa_sharik["speedy_padenie"] = -2
            infa_sharik["coord"][1] = 750 - infa_sharik["radius"]

        if infa_sharik["coord"][0] >= 400 and infa_sharik["coord"][0] <= 500 and infa_sharik["coord"][1] >= 750 - \
                infa_sharik["radius"]:
            l = infa_sharik["coord"][0] - 400
            l = l * 0.02
            infa_sharik["speedy_padenie"] = -4 + l

        if infa_sharik["coord"][0] > 300 and infa_sharik["coord"][0] <= 400 and infa_sharik["coord"][1] >= 750 - \
                infa_sharik["radius"]:
            l = 400 - infa_sharik["coord"][0]
            l = l * 0.02
            infa_sharik["speedy_padenie"] = -4 + l

        infa_sharik["speedy_padenie"] += 0.05
