import pygame,random

all_sharik = []
sharik_per_second = 0
alpha = 180
visible_settings = True

def dvizhenie_sharov():
    for infa_sharik2 in all_sharik:
        if infa_sharik2["coord"][1] + infa_sharik2["radius"] >= 750:#низ
            infa_sharik2["speedy"] *= -1

        if infa_sharik2["coord"][1] - infa_sharik2["radius"] <= 0:#верх
            infa_sharik2["speedy"] *= -1

        if infa_sharik2["coord"][0] + infa_sharik2["radius"] >= 750:#право
            infa_sharik2["speedx"] *= -1

        if infa_sharik2["coord"][0] - infa_sharik2["radius"] <= 0:#лево
            infa_sharik2["speedx"] *= -1

        infa_sharik2["coord"][0] += infa_sharik2["speedx"]
        infa_sharik2["coord"][1] += infa_sharik2["speedy"]



